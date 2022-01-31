from bottle import route, static_file

@route('/')
def index():
    return server_static('index.html')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='../static')
