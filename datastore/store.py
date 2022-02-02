import os.path
import json
from sqlite3 import Error
from datastore.connection import Connection


class Store:

    @staticmethod
    def migrate_db(conf):
        # todo check max version -> prevent duplicate migration
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def check_schema_version(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def execute_migration(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)



