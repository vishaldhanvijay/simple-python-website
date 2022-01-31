from bottle import post, request, response, view, template
from datastore import users
from data.config import Config


def check_login(db, username, password):
    row = db.execute('SELECT username, password from users where username=?', (username,)).fetchone()
    if row:
        return users.verify_hash(Config.config, password, row['password'])
    return False


#@view('login_result')
@post('/login')
def do_login(db):
    username = request.forms.get('username')
    password = request.forms.get('password')
    name = None
    if check_login(db, username, password):
        name = users.get_user(db, username)
        cookie_content = {
            'username': username,
            'client-ip': request.remote_addr,
            'real-name': name
        }
        response.set_cookie("account", cookie_content, secret=Config.config.cookie_secret, max_age=10)

    return template('login_result', dict(username=username, name=name))
