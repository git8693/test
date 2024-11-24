import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x8aLY\xc4\x0e<\xf8\xcb@\xb6\xf5\xc8\x0f\xd3\x03\xa6'

    MONGODB_SETTINGS = {
                        'db' : 'risiko',
                        'host' : 'mongodb://localhost:27017/risiko'
                       }
    