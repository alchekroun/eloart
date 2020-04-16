import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Set Flask configuration vars"""

    SECRET_KEY = os.environ.get('SECRET_KEY')
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SESSION_PERMANENT = os.environ.get('SESSION_PERMANENT')
    SESSION_TYPE = os.environ.get('SESSION_TYPE')

    # Database
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_DB = os.environ.get('MYSQL_DB')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')