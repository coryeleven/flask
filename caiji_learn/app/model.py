# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 5:06 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : model.py
# @Software : PyCharm
from . import db

# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(64), nullable=False, unique=True)  # 账号
    password = db.Column(db.String(64), nullable=False)  # 密码
    phone = db.Column(db.String(11))  # 手机号



# 管理员表
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(64), nullable=False, unique=True)  # 账号
    password = db.Column(db.String(64), nullable=False)  # 密码
    power = db.Column(db.Enum('管理员', '超级管理员'), nullable=False, default='管理员')
    phone = db.Column(db.String(11))  # 手机号
    address = db.Column(db.String(128))  # 地址
