import os


class Config:

    ENV_DB_FILENAME = 'SPW_DB_FILENAME'
    ENV_MIGRATIONS_DIRECTORY = 'SPW_MIGRATIONS_DIRECTORY'
    ENV_COOKIE_SECRET = 'SPW_COOKIE_SECRET'
    ENV_PASSWORD_SECRET = 'SPW_PASSWORD_SECRET'

    def __init__(self,
                 db_filename='../data/database/test1.db',
                 migrations_directory='../data/migrations',
                 cookie_secret='some-secret-value',
                 password_secret='some-other-secret-value'):
        self.db_filename = os.getenv(Config.ENV_DB_FILENAME) or db_filename
        self.migrations_directory = os.getenv(Config.ENV_MIGRATIONS_DIRECTORY) or migrations_directory
        self.cookie_secret = os.getenv(Config.ENV_COOKIE_SECRET) or cookie_secret
        self.password_secret = os.getenv(Config.ENV_PASSWORD_SECRET) or password_secret





