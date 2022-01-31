from bottle import route, static_file
from data.config import Config


@route('/')
def index():
    return server_static('index.html')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=Config.config.static_files_directory)
