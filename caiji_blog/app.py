# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 12:36 上午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import redis
from flask_session import Session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@cory.net.cn:3306/caiji_dev'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"
db = SQLAlchemy(app)  # 实例化的数据库

# flask-session配置
app.config['SESSION_TYPE'] = "redis"
app.config['SESSION_USE_SIGNER'] = True  # 对cookie中session_id进行隐藏处理 加密混淆
app.config['PERMANENT_SESSION_LIFETIME'] = 20  # session数据的有效期，单位秒
app.config['SESSION_REDIS'] = redis.Redis(host='cory.net.cn', port=6379, password="Cory#123", db=1)  # 操作的redis配置
Session(app)

# 注册蓝图
from flask_project.caiji_blog.admin import admin
# from flask_project.caiji_blog.main import main

# app.register_blueprint(main, url_prefix="/main")  # 绑定包里面的蓝图对象
app.register_blueprint(admin, url_prefix="/admin")

if __name__ == '__main__':
    app.run(debug=True)
