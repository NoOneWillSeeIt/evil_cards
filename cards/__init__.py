# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cards.config import config


app = Flask(__name__)
config_name = os.environ.get('FLASK_CONFIG') or 'def'
app.config.from_object(config[config_name])

db = SQLAlchemy(app)

from cards import routes
