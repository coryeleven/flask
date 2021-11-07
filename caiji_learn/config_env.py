# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 5:29 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : config.py
# @Software : PyCharm
import redis


class Config(object):
    # 数据库配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "caiji"

    # session存到redis
    # flask-session配置
    SESSION_TYPE = "redis"  # 存session到redis
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理 加密混淆
    PERMANENT_SESSION_LIFETIME = 20  # session数据的有效期，单位秒


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@cory.net.cn:3306/caiji_dev'
    SESSION_REDIS = redis.Redis(host='cory.net.cn', password='Cory#123', port=6379, db=1)
    DEBUG = True


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@cory.net.cn:3306/caiji_prod'
    SESSION_REDIS = redis.Redis(host='cory.net.cn', password='Cory#123', port=6379, db=2)
    DEBUG = True


config_map = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
}
