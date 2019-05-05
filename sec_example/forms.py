#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/14 13:25
# @Author : Am4zing
# @Site :
# @File : views.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    verify_code = StringField('验证码', validators=[DataRequired()])
    submit = SubmitField('登录')
