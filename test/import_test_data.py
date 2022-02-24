from datastore.store import Store
from data.config import Config
import os

test_data_directory = 'test/test_data/'


def import_things(file_name='things.json'):
    things_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(Config.config, 'things', things_file)


Config()
Store.migrate_db(Config.config)
import_things()

