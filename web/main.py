from bottle import run, install
from bottle_sqlite import SQLitePlugin
from data.config.config import Config
from store.store import Store
from store.connection import Connection
import api.login
import app.main
import hello
import errors

config = Config()

with Connection(config) as conn:
    config = Config()
    Store.migrate_db(config)

install(SQLitePlugin(dbfile=config.db_filename))

run(host='localhost', port=9999)
