#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : settings.py 
# @Software: PyCharm

import os

dev_db = "mysql+pymysql://root:root@127.0.0.1:52206/sec_example"

SECRET_KEY = os.getenv('SECRET_KEY', 'afsdfasdfasdfasdfasdfasdfasdf')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


Debug = True
