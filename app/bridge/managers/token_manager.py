import uuid


def generate_md5_token(namespace, name):
    return str(uuid.uuid3(namespace, name)).replace('-','')


def generate_random_token():
    return str(uuid.uuid4()).replace('-','')
