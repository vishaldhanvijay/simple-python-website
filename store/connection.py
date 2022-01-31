import sqlite3
from sqlite3 import Error


class Connection:
    def __init__(self, config):
        self.config = config
        self.max_connections = 5
        self.reserved_connections = []
        self.available_connections = []
        self.connection = None

    def __enter__(self):
        self.connection = self.create_connection()
        return self.connection

    def __exit__(self):
        self.connection.close()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.config.db_filename)
            return conn
        except Error as e:
            print(e)

        return conn

    def get_connection(self):
        conn = None
        if len(self.available_connections) > 0:
            conn = self.available_connections[0]
            self.available_connections.remove(conn)
            self.reserved_connections.append(conn)
        elif len(self.reserved_connections) < self.max_connections:
            conn = self.create_connection()
            self.reserved_connections.append(conn)
        return conn

    def release_connection(self, conn):
        self.reserved_connections.remove(conn)
        self.available_connections.append(conn)

    def close_connection(self, conn):
        if conn is None:
            return
        if conn in self.reserved_connections:
            self.reserved_connections.remove(conn)
        if conn in self.available_connections:
            self.available_connections.remove(conn)
        conn.close()

