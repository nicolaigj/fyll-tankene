import os
"""Local config is not committed to source control, please create a local_config.py with the 
properties imported from local_config.
"""
from local_config import DATABASE_USER, DATABASE_PASSWORD, LOCAL_SECRET_KEY
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost/fylltankene'.format(DATABASE_USER, DATABASE_PASSWORD)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = LOCAL_SECRET_KEY