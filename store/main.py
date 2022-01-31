from data.config.config import Config
from connection import Connection
import migrate
import users

class Store:

    instance = None

    def __init__(self, config):
        self.connection_pool = Connection(config)
        db_connection = self.connection_pool.get_connection()
        migrate.migrate_db(db_connection, config.migrations_directory)
        self.connection_pool.close_connection(db_connection)
        Store.instance = self

    def get_connection(self):
        self.connection_pool.get_connection()


if __name__ == '__main__':
    store = Store(Config())


