from bottle import post, request, response, template
from datastore import users
from data.config import Config


def check_login(db, username, password):
    row = db.execute('SELECT username, password from users where username=?', (username,)).fetchone()
    if row:
        print(f"found user: {row['username']}")
        return users.verify_hash(Config.config, password, row['password'])
    return False


@post('/login')
def do_login(db):
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(db, username, password):
        cookie_content = {
            'username': username,
            'client-ip': request.remote_addr
        }
        response.set_cookie("account", cookie_content, secret='some-secret-key', max_age=10)
        return template("<p>Welcome {{name}}! You are now logged in.</p>"
                        "<p>Please proceed to the <a href=\"/restricted\">RESTRICTED AREA</a>.</p>", name=username)
    else:
        return "<p>Login failed.</p>"
