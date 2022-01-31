from bottle import get, post, request, response, route, template, error


def check_login(username, password):
    print(f'{username} {password}')
    return username == 'Jarkko' and password == 'Lakso'


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
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
    if cookie_content:
        username = cookie_content['username']
        client_ip = cookie_content['client-ip']
    if username:
        return template("Hello {{name}} from {{ip}}. Welcome back.", name=username, ip=client_ip)
    else:
        return "You are not logged in. Access denied. <p><a href=\"/login\">Login</a></p>"

