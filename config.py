"""app configuration """
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = True
    TESTING = False
    SECRET = 'werdtfyug45678fgut4547gihnhpih'

class Development(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URL = os.getenv('api_database_url')

class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URL = os.getenv('test_database_url')

class Production(Config):
    """Configurations for Production."""
    DEBUG = False

app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}

