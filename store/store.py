import os.path
from sqlite3 import Error
from data.config.config import Config
from connection import Connection
import json


class Store:

    @staticmethod
    def migrate_db(conf):
        # for file in files
        file = os.path.join(conf.migrations_directory, 'migrations.json')
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data is not None:
            for m in data["migrations"]:
                Store.execute_migration(m, conf)

    @staticmethod
    def execute_migration(migration, conf):
        print(f'Executing:\n{migration}')
        with Connection(conf) as db_connection:
            try:
                print(f'still connected to {db_connection}')
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', current_date);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)


if __name__ == '__main__':
    config = Config()
    Store.migrate_db(config)





