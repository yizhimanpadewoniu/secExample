#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 15:46 
# @Author : Am4zing
# @Site :  
# @File : models.py 
# @Software: PyCharm

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


from datetime import datetime
from sec_example import db


class sort_info(db.Model):
    __tablename__ = 'sort_info'
    sort_no = db.Column(db.Integer, primary_key=True)
    sort = db.Column(db.String(255))
    vuln_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    demo_url = db.Column(db.String(255))

class User(db.Model):
    __tablename__ = 'User'
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    role = db.Column(db.String(255))
    phone = db.Column(db.String(11))

class user_info(db.Model):
    __tablename__ = 'user_info'
    email = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255))
    role = db.Column(db.String(255))
    phone = db.Column(db.String(255))

def validate_picture():
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 图片大小130 x 50
    width = 130
    heighth = 50
    # 先生成一个新图片对象
    im = Image.new('RGB',(width, heighth), 'white')
    # 设置字体
    font = ImageFont.truetype(r"C:\Windows\Fonts\FreeSans.ttf", 40)
    # 创建draw对象
    draw = ImageDraw.Draw(im)
    str = ''
    # 输出每一个文字
    for item in range(4):
        text = total[random.randint(0, (len(total)-1))]
        str += text
        draw.text((5+random.randint(4,7)+20*item,5+random.randint(3,7)), text=text, fill='black',font=font )

    # 划几根干扰线
    for num in range(8):
        x1 = random.randint(0, width/2)
        y1 = random.randint(0, heighth/2)
        x2 = random.randint(0, width)
        y2 = random.randint(heighth/2, heighth)
        draw.line(((x1, y1),(x2,y2)), fill='black', width=1)

    # 模糊下,加个帅帅的滤镜～
    im = im.filter(ImageFilter.FIND_EDGES)
    return im, str
