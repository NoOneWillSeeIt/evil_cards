# -*- coding: utf-8 -*-
import os


class Config:
    SECRET_KEY = '4dc9320e402e8c7ea6b29c5a4f7f889e'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///static/site.db'


class HerokuConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'def': Config(),
    'heroku': HerokuConfig(),
}
