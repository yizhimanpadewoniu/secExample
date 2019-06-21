#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : settings.py 
# @Software: PyCharm

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# HOSTNAME = '127.0.0.1'
# PORT = '52206'
# DATABASE = 'sec_example'
# USERNAME = 'root'
# PASSWORD = 'root'
#
# DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
#
# engine = create_engine(DB_URI)
# Base = declarative_base(engine)

# dev_db = "mysql+pymysql://root:root@127.0.0.1:52206/sec_example"
# dev_db = "mysql+pymysql://root:root@172.18.62.46:3306/sec_example"

SECRET_KEY = os.getenv('SECRET_KEY', 'afsdfasdfasdfasdfasdfasdfasdf')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


# Debug = True

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True


class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')
    # QLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
    dev_db = "mysql+pymysql://root:123@172.18.62.75:3306/sec_example"
    # dev_db = "mysql+pymysql://root:root@127.0.0.1:52206/sec_example"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    dev_db = "mysql+pymysql://root:123@172.18.62.75:3306/sec_example"
    # dev_db = "mysql+pymysql://root:root@127.0.0.1:52206/sec_example"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    'production': ProductionConfig
}