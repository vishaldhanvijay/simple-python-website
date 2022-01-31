from bottle import get, request, route, template, view
from data.config import Config


@get('/login')
def login():
    return template('login_form')


@route('/restricted')
@view('restricted')
def restricted_area():
    cookie_content = request.get_cookie("account", secret=Config.config.cookie_secret)
    username = None
    name = None
    client_ip = None
    if cookie_content:
        username = cookie_content['username']
        client_ip = cookie_content['client-ip']
        name = cookie_content['real-name']

    return dict(name=name, ip=client_ip)

