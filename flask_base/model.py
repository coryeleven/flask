# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 2:27 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : sqlalchemy_app.py
# @Software : PyCharmi
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)
# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@cory.net.cn:3306/ops'
# 跟踪数据库修改,不建议修改
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

"""
_sqlalchemy 中默认使用 MySQLdb 连接数据库
而这个包仅支持py2语法，所以要单独安装 pymysql 并使用它作为flask_sqlalchemy连接的内核。
"""
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


# 数据库模型定义，需要继承db.Model
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段，db.Column表示一个字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=True)
    # 在一的一方，写关联，db.relationship('User')表示和User模型发生了关联，增加了users属性
    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    # db.Foreignkey表明外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))




if __name__ == '__main__':
    app.run(debug=True)
