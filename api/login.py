from bottle import post, request, response
from datastore import users
from data.config import Config


def check_login(db, username, password):
    row = db.execute('SELECT username, password from users where username=?', (username,)).fetchone()
    if row:
        return users.verify_hash(Config.config, password, row['password'])
    return False


@post('/login')
def do_login(db):
    username = request.json.get('username')
    password = request.json.get('password')
    login_success = check_login(db, username, password)
    if login_success:
        name = users.get_name_by_username(db, username)
        cookie_content = {
            'username': username,
            'client-ip': request.remote_addr,
            'real-name': name
        }
        response.set_cookie("account", cookie_content, secret=Config.config.cookie_secret, max_age=Config.config.session_ttl)

    response.headers['Content-type'] = 'application/json'
    return dict(login_success=login_success)

