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

dev_db = "mysql+pymysql://root:root@127.0.0.1:52206/sec_example"
# dev_db = "mysql+pymysql://root:root@172.18.62.46:3306/sec_example"

SECRET_KEY = os.getenv('SECRET_KEY', 'afsdfasdfasdfasdfasdfasdfasdf')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


Debug = True
