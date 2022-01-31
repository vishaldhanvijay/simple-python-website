import sqlite3
from sqlite3 import Error
import os


class Connection(object):
    def __init__(self, conf):
        self.config = conf
        self.database_filename = file = os.path.join(conf.data_directory, conf.db_filename)
        self.db_connection = None

    def __enter__(self):
        self.db_connection = self.create_connection()
        print(f'created connection: {self.db_connection}')
        return self.db_connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_value)
        print(exc_type)
        print(traceback)
        self.db_connection.commit()
        self.db_connection.close()
        print(f'closed connection: {self.db_connection}')

    def create_connection(self):
        conn = None
        try:
            print(f'Connecting {self.config.db_filename}')
            conn = sqlite3.connect(self.config.db_filename)
            return conn
        except Error as e:
            print(e)
        return conn
