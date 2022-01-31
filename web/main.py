import os
from bottle import run, install
from bottle_sqlite import SQLitePlugin
from data.config import Config
from datastore.store import Store
import app
import api


Config()
Store.migrate_db(Config.config)

database_filename = os.path.join(Config.config.data_directory, Config.config.db_filename)
install(SQLitePlugin(dbfile=database_filename))

run(host='localhost', port=Config.config.port)
