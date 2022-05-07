import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "You can't guess it!"
    TEMPLATES_AUTO_RELOAD = True