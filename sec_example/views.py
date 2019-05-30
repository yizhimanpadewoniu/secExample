#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : views.py 
# @Software: PyCharm

from flask import render_template, url_for, make_response, session, flash, redirect, request, get_flashed_messages, jsonify
from io import BytesIO
from sec_example import app, db, forms, models
from sec_example.models import validate_picture
from sec_example.models import User, user_info, sort_info
from sqlalchemy import exists, or_


@app.route('/', methods=['GET'])
def index():
    # SortInfo.
    info_datas = sort_info.query.order_by(sort_info.timestamp.desc()).all()
    return render_template('index.html', messages=info_datas)

# 默认图形验证码生成
@app.route('/code')
def get_code():
    image, str = validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    response.headers['ImgContent-Text'] = '%s' % str
    # 将验证码字符串储存在session中
    session['image'] = str
    return response


# 图形验证码泄露
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('用户不存在，请使用admin@yeepay.com登陆.', category='User_Exist')
            return render_template('login.html', form=form)
        if session.get('image') != form.verify_code.data:
            flash(u'验证码错误.', category='verify_code_error')
            return render_template('login.html', form=form)
        # elif user is not None and user.verify_password(form.password.data):
        if User.query.filter_by(password=form.password.data).first() is not None:
            flash(u'验证通过，登录成功!', category='OK')
            # return redirect('login.html')
        else:
            flash(u'用户名或者密码不正确', category='No_Pass')
    return render_template('login.html', form=form)


# 图形验证码重复使用——生成图形验证码
@app.route('/vgcode')
def get_vgcode():
    ag_image, ag_str = validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    ag_buf = BytesIO()
    ag_image.save(ag_buf, 'jpeg')
    ag_buf_str = ag_buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(ag_buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = ag_str
    return response


# # 图形验证码重复使用
@app.route('/invalid', methods=['GET', 'POST'])
def invalid():
    invali_form = forms.LoginForm()
    if invali_form.validate_on_submit():
        user = User.query.filter_by(email=invali_form.email.data).first()
        if user is None:
            flash('用户不存在，请使用admin@yeepay.com登陆.', category='User_Exist')
            return render_template('invalid.html', form=invali_form)
        if session.get('image') != invali_form.verify_code.data:
            flash(u'验证码错误.', category='verify_code_error')
            # return render_template('again.html', form=again_form)
        if User.query.filter_by(password=invali_form.password.data).first() is not None:
            flash(u'验证通过，登录成功!', category='OK')
        else:
            flash(u'用户名或者密码不正确', category='No_Pass')
    return render_template('again.html', form=invali_form)

#
@app.route('/leak', methods=['GET', 'POST'])
def leak():
    leak_form = forms.AcctQueryForm()
    if leak_form.validate_on_submit():
        user = user_info.query.filter(user_info.email==leak_form.email.data).all()
        print(user)
        print(type(user))
        if user is None:
            flash('用户不存在。', category='User_Exist')
            return render_template('leak.html', form=leak_form)
        else:
            flash('用户存在')
            response_data = user
            print(response_data)
            # return jsonify(response_data)
    return render_template('leak.html', form=leak_form)

@app.route('/imgdos')
def imgdos():
    return "<h1>imgdos</h1>"

@app.route('/agcode')
def get_agcode():
    ag_image, ag_str = validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    ag_buf = BytesIO()
    ag_image.save(ag_buf, 'jpeg')
    ag_buf_str = ag_buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(ag_buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = ag_str
    return response

@app.route('/again')
def again():
    return "<h1>img invalid</h1>"