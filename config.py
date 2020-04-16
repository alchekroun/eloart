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
