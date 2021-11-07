# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 5:06 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : __init__.py.py
# @Software : PyCharm
import redis as redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from config_env import config_map

db = SQLAlchemy()  # 没有参数的实例化数据库对象


# 返回一个实例化并且配置好数据的一个app,env_name代表环境的配置名称
def create_app(env_name):
    app = Flask(__name__)
    config_class = config_map.get(env_name)
    app.config.from_object(config_class)  # 从类中读取配置信息

    db.init_app(app)  # 实例化数据库对象

    Session(app)  # 利用flask-session，将session数据保存到redis

    # 注册蓝图
    from .api import user, admin

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(admin, url_prefix='/admin')
    return app
