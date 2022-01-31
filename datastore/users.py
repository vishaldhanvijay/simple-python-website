import hashlib


def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def verify_hash(config, password, password_hash):
    calculated_hash = calculate_password_hash(config, password)
    if calculated_hash == password_hash:
        return True
    else:
        return False



