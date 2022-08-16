import os
import subprocess
basedir = os.path.abspath(os.path.dirname(__file__))
process = subprocess.Popen(['yc', 'iam', 'create-token'], stdout=subprocess.PIPE, text=True)
result = process.communicate()[0].rstrip()
os.environ['TRANSLATOR_KEY'] = result


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'localhost'  # os.environ.get('MAIL_SERVER')
    MAIL_PORT = 8025  # int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = None  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = None  # os.environ.get('MAIL_PASSWORD')
    ADMINS = ['prorok2000@inbox.ru']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'ru']
    TRANSLATOR_KEY = os.environ.get('TRANSLATOR_KEY')
