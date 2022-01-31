import os.path
import sqlite3
from sqlite3 import Error


def migrate_db(db_connection, migrations_directory):

    file = os.path.join(migrations_directory, 'V__1__initial_migration.sql')
    sql = None
    with open(file, 'r') as f:
        sql = f.read()

    if sql is not None:
        for s in sql.split(';'):
            try:
                print(f'Executing:\n{s}')
                c = db_connection.cursor()
                c. execute(s)
            except Error as e:
                print(e)

