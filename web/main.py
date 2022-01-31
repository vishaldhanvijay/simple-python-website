from bottle import run, install
from bottle_sqlite import SQLitePlugin
from data.config import Config
from datastore.store import Store

Config()
Store.migrate_db(Config.config)

install(SQLitePlugin(dbfile=Config.config.db_filename))

run(host='localhost', port=9999)
