#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:13 
# @Author : Am4zing
# @Site :  
# @File : __init__.py.py 
# @Software: PyCharm

import os

from flask import Flask
from sec_example.extensions import db
from sec_example.settings import config
# from sec_example.views import sec_app

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('sec_example')
    app.config.from_object(config[config_name])

    register_extension(app)
    # register_views(app)

    return app

def register_extension(app):
    db.init_app(app)

# def register_views(app):
    # sec_app(app)
    # app = Flask('sec_example')
    # app.config.from_pyfile('settings.py')
    # app.jinja_env.trim_blocks = True
    # app.jinja_env.lstrip_blocks = True
    #



from sec_example import views, settings
