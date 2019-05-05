#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : views.py 
# @Software: PyCharm

from flask import render_template, url_for, make_response, session, flash, redirect, request
from io import BytesIO
from sec_example import app, db, forms, models
from sec_example.models import sort_info


@app.route('/', methods=['GET'])
def index():
    # SortInfo.
    info_datas = sort_info.query.order_by(sort_info.timestamp.desc()).all()
    return render_template('index.html', messages=info_datas)

@app.route('/code')
def get_code():
    image, str = models.validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = str
    return response

@app.route('/login', methods=['POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if session.get('image') != form.verify_code.data:
            flash('验证码错误')
        # 验证用户的登录密码
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('验证通过，登录成功')
            return redirect(request.args.get('next') or
                            url_for('main.index'))
        else:
            flash('用户名或者密码不正确')
    return render_template('auth/login.html', form=form)

