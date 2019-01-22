from urllib.parse import urlparse
import os

def database_configuration():
    db_config = os.getenv('api_database_url')
    response = urlparse(db_config)
    config = {
        'database': response.path[1:],
        'user': response.username,
        'password': response.password,
        'host': response.hostname
        }
    return config