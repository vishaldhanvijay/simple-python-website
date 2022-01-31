import os


class Config:

    ENV_DATABASE_FILENAME = 'SPW_DATABASE_FILENAME'
    ENV_MIGRATIONS_FILENAME = 'SPW_MIGRATIONS_FILENAME'
    ENV_DATA_DIRECTORY = 'SPW_DATA_DIRECTORY'
    ENV_STATIC_FILES_DIRECTORY = 'SPW_STATIC_FILES_DIRECTORY'
    ENV_COOKIE_SECRET = 'SPW_COOKIE_SECRET'
    ENV_PASSWORD_SECRET = 'SPW_PASSWORD_SECRET'

    config = None

    def __init__(self,
                 database_filename='test1.db',
                 migrations_filename='migrations.json',
                 data_directory='/home/jarkko/git/simple-python-website/data',
                 static_files_directory='/home/jarkko/git/simple-python-website/static',
                 cookie_secret='some-secret-value',
                 password_secret='some-other-secret-value'):
        self.db_filename = os.getenv(Config.ENV_DATABASE_FILENAME) or database_filename
        self.migrations_filename = os.getenv(Config.ENV_MIGRATIONS_FILENAME) or migrations_filename
        self.data_directory = os.getenv(Config.ENV_DATA_DIRECTORY) or data_directory
        self.static_files_directory = os.getenv(Config.ENV_STATIC_FILES_DIRECTORY) or static_files_directory
        self.cookie_secret = os.getenv(Config.ENV_COOKIE_SECRET) or cookie_secret
        self.password_secret = os.getenv(Config.ENV_PASSWORD_SECRET) or password_secret
        Config.config = self
