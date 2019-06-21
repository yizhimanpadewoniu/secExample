#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/14 13:25
# @Author : Am4zing
# @Site :
# @File : sec_views.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1, 64), Email()], default=None, id='user_email')
    password = PasswordField('密码', validators=[DataRequired()], default=None, id='user_passwd')
    verify_code = StringField('验证码', validators=[DataRequired(), Length(1,5)], default=None, id='verify_code')
    submit = SubmitField('登录')


class AcctQueryForm(FlaskForm):
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1,64), Email()], default=None, id='username')
    submit = SubmitField('查询')


class UserInfoQuery(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1,64)], default=None, id='username')
    submit = SubmitField('查询')


class YqcxInfoQuery(FlaskForm):
    email = SubmitField('电子邮箱', validators=[DataRequired(), Length(1, 64), Email()], default=None, id='user_email')
    submit = SubmitField('查询')


class Captcha_again(FlaskForm):
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1, 64), Email()], default=None, id='user_email')
    password = PasswordField('密码', validators=[DataRequired()], default=None, id='user_passwd')
    verify_code = StringField('验证码', validators=[DataRequired(), Length(1, 5)], default=None, id='verify_code')
    submit = SubmitField('登录')