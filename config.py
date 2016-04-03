import os
from settings import settings

basedir = os.path.abspath(os.path.dirname(__file__))


def get_postgresql_url():
    return 'postgres://{user}:{password}@{host}:{port}/{database}'.format(
        database=settings.get('database'),
        user=settings.get('user'),
        password=settings.get('password'),
        host=settings.get('host'),
        port=5432,
    )

SQLALCHEMY_DATABASE_URI = get_postgresql_url()
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
