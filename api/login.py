from bottle import get, post, request, response, route, template
from datastore import users
from data.config import Config


def check_login(db, username, password):
    row = db.execute('SELECT username, password from users where username=?', (username,)).fetchone()
    if row:
        print(f"found user: {row['username']}")
        return users.verify_hash(Config.config, password, row['password'])
    return False


@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


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


@route('/restricted')
def restricted_area():
    cookie_content = request.get_cookie("account", secret='some-secret-key')
    username = None
    client_ip = None
    if cookie_content:
        username = cookie_content['username']
        client_ip = cookie_content['client-ip']
    if username:
        return template("Hello {{name}} from {{ip}}. Welcome back.", name=username, ip=client_ip)
    else:
        return "You are not logged in. Access denied. <p><a href=\"/login\">Login</a></p>"

