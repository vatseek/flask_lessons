import os

settings = {
    'database': os.environ.get('POSTGRESQL_DATABASE', 'flax'),
    'user': os.environ.get('POSTGRESQL_USER', 'flax'),
    'password': os.environ.get('POSTGRESQL_PASSWORD', 'qwerty'),
    'host': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
}
