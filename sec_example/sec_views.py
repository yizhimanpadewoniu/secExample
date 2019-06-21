#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 13:25 
# @Author : Am4zing
# @Site :  
# @File : sec_views.py
# @Software: PyCharm

from flask import render_template, url_for, make_response, session, flash
from flask import Blueprint
from io import BytesIO
from sec_example.extensions import db
from sec_example import forms, zlcache
from sec_example.models import validate_picture
from sec_example.models import User, User_info, sort_info, Yqcx_info, User_login

sec_bp = Blueprint('sec_views', __name__)

@sec_bp.route('/', methods=['GET'])
def index():
    # SortInfo.
    info_datas = sort_info.query.order_by(sort_info.timestamp.desc()).all()
    return render_template('index.html', messages=info_datas)

# 默认图形验证码生成
@sec_bp.route('/code')
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
@sec_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('用户不存在，请使用admin@qq.com登陆.', category='User_Exist')
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


# 图形验证码失效——生成图形验证码
@sec_bp.route('/invalid_code')
def get_invalid_gcode():
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


# 图形验证码失效invalid
@sec_bp.route('/invalid', methods=['GET', 'POST'])
def invalid():
    invalid_form = forms.LoginForm()
    if invalid_form.validate_on_submit():
        user = User.query.filter_by(email=invalid_form.email.data).first()
        if user is None:
            flash('用户不存在，请使用admin@qq.com登陆.', category='User_Exist')
            return render_template('invalid.html', form=invalid_form)
        if session.get('image') != invalid_form.verify_code.data:
            flash(u'验证码错误.', category='verify_code_error')
            # return render_template('again.html', form=again_form)
        if User.query.filter_by(password=invalid_form.password.data).first() is not None:
            flash(u'验证通过，登录成功!', category='OK')
        else:
            flash(u'用户名或者密码不正确', category='No_Pass')
    return render_template('invalid.html', form=invalid_form)

# 多余信息泄露

@sec_bp.route('/info_query')
def info_query(post_data):
    user = db.session.query(User_info).filter(User_info.email == post_data.email.data).first()
    if user is None:
        flash_message = '用户不存在'
        category = 'User_Exist'
        # response = jsonify(name_email=user.email, username=user.username, user_role=user.role, user_phone=user.phone)
        result = {'flash_message':flash_message, "category":category, "response":''}
        return result
    else:
        response = {"name_email":user.email, "username":user.username, "user_role":user.role, "user_phone":user.phone}
        flash_message = '用户存在'
        category = 'User_Exist'
        result = {'flash_message': flash_message, "category": category, "response": response}
        return result

@sec_bp.route('/leak', methods=['POST', 'GET'])
def leak():
    leak_form = forms.AcctQueryForm()
    if leak_form.validate_on_submit():
        if leak_form.email is not '':
            query_data = info_query(leak_form)
            messages = query_data['response']
            flash(query_data['flash_message'], category=query_data['category'])
            return render_template('leak.html', form=leak_form, messages=messages)
        else:
            query_data = info_query(leak_form)
            messages = query_data['response']
            flash(query_data['flash_message'], category=query_data['category'])
            return render_template('leak.html', form=leak_form, messages=messages)
    else:
        flash('请输入需要查询的用户名，eg: admin@qq.com')
        return render_template('leak.html', form=leak_form)

# 水平越权查询

@sec_bp.route('/yqcx_info_query')
def yqcx_info_query(post_data):
    user = db.session.query(Yqcx_info).filter(Yqcx_info.email == post_data.email.data).first()
    if user is None:
        flash_message = '用户不存在'
        category = 'User_Exist'
        result = {"flash_message":flash_message, "category":category, "response":''}
        return result
    else:
        response = {"user_email": user.email, "username": user.username, "user_phone": user.phone, "user_id": user.id_card, "company": user.company, "address": user.address}
        flash_message = '用户存在'
        category = 'User_Exist'
        result = {"flash_message": flash_message, "category": category, "response": response}
        return result


@sec_bp.route('/yqcx', methods=['POST'])
def yqcx():
    yqcx_form = forms.YqcxInfoQuery()
    if yqcx_form.validate_on_submit():
        yqcx_query_data = url_for('info_query')
        print(yqcx_query_data)
        if yqcx_form.email is not '':
            query_data = info_query(yqcx_form)
            messages = query_data['response']
            flash(query_data['flash_message'], category=query_data['category'])
            return render_template('leak.html', form=yqcx_form, messages=messages)
        else:
            query_data = info_query(yqcx_form)
            messages = query_data['response']
            flash(query_data['flash_message'], category=query_data['category'])
            return render_template('leak.html', form=yqcx_form, messages=messages)
    else:
        flash('请输入需要查询的用户邮箱')
        return render_template('yqcq.html', form=yqcx_form)

#图形验证码DOS

@sec_bp.route('/imgdos')
def imgdos():
    return "<h1>imgdos</h1>"

# 图形验证码重复使用

@sec_bp.route('/agcode')
def get_agcode():
    ag_image, ag_str= validate_picture()
    zlcache.set(ag_str.lower(), ag_str.lower())
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    ag_buf = BytesIO()
    ag_image.save(ag_buf, 'jpeg')
    ag_buf_str = ag_buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(ag_buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中    session['image'] = ag_str
    return response


@sec_bp.route('/again', methods=['GET', 'POST'])
def again():
    again_form = forms.Captcha_again()
    if again_form.validate_on_submit():
        # user = User.query.filter_by(email=again_form.email.data).first()
        user = db.session.query(User_login).filter(User_login.email == again_form.email.data).first()
        if user is None:
            flash('用户不存在，请使用admin@qq.com登陆.', category='User_Exist')
            return render_template('again.html', form=again_form)
        if db.session.query(User_login).filter_by(password=again_form.password.data).first() is not None:
        # if User.query.filter_by(password=again_form.password.data).first() is not None:
            flash(u'验证通过，登录成功!', category='OK')
        if zlcache.get(again_form.verify_code.data) != again_form.verify_code.data:
            flash(u'验证码错误.', category='verify_code_error')
            # return render_template('again.html', form=again_form)
        else:
            flash(u'密码不正确', category='No_Pass')
    return render_template('again.html', form=again_form)


