#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : settings.py 
# @Software: PyCharm

import os

SECRET_KEY = os.getenv('SECRET_KEY', 'afsdfasdfasdfasdfasdfasdfasdf')

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True


class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')
    dev_db = "mysql+pymysql://root:root@127.0.0.1:3306/sec_example"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    dev_db = "mysql+pymysql://root:root@127.0.0.1:3306/sec_example"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    'production': ProductionConfig
}