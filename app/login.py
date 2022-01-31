from bottle import get, request, route, template


@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


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

