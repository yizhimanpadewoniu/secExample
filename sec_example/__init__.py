#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:13 
# @Author : Am4zing
# @Site :  
# @File : __init__.py.py 
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app = Flask('sec_example')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


from sec_example import views, settings
