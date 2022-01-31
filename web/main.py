from bottle import run, error, install
from bottle_sqlite import SQLitePlugin
from data.config.config import Config
import api.login
import app.main
import hello

install(SQLitePlugin(dbfile=Config.db_filename))


@error(404)
def error404(error):
    return 'Nothing here, sorry'


@error(500)
def error500(error):
    return 'Oops!'


run(host='localhost', port=9999)
