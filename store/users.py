import hashlib
from store.main import Store


def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def verify_hash(config, password, password_hash):
    if password_hash == calculate_password_hash(config, password):
        return True
    else:
        return False


def verify_user(username):
    # conn = Store.instance.get_connection()
    return True



