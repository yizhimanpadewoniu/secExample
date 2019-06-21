#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/14 13:25
# @Author : Am4zing
# @Site :
# @File : sec_views.py
# @Software: PyCharm

import memcache

pic_cache = memcache.Client(["172.18.62.75:11211"], debug=True)

def set(key,value,timeout=600):
    return pic_cache.set(key,value,timeout)

def get(key):
    return pic_cache.get(key)

def delete(key):
    return pic_cache.delete(key)
