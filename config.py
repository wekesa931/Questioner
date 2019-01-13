"""app configuration """
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = True
    TESTING = False

class Development(Config):
    """Configurations for Development."""
    TESTING = True

class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True

class Production(Config):
    """Configurations for Production."""
    DEBUG = False

app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}