# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 5:06 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : api.py
# @Software : PyCharm
from flask import Blueprint, request, jsonify, session
from . import db
from .model import User, Admin

user = Blueprint('user', __name__)
admin = Blueprint('admin', __name__)


# 用户成功响应
@user.route('/index', methods=['GET'])
def hello_world():
    return 'Hello Cory! 这里是用户响应！！'


# 用户注册
@user.route('/register', methods=['POST'])
def user_register():
    try:
        my_json = request.get_json()
        print(my_json)
        username = my_json.get("username")
        password = my_json.get("password")
        if not all([username, password]):
            return jsonify(code='4000', msg='参数不完整')
        user = User(username=username, password=password)
        # 添加到数据库
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(code=200, msg='注册成功', username=username)
        except Exception as e:
            print(e)
            return jsonify(msg=e, code=4001)
    except Exception as e:
        print(e)
        return jsonify(msg='存数据失败', code=4001)


# 用户登录
@user.route("/login", methods=["POST"])
def user_login():
    get_data = request.get_json()
    print(get_data)
    username = get_data.get("username")
    password = get_data.get("password")
    if not all([username, password]):
        return jsonify(msg="参数不完整")
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        # 如果验证通过 保存登录状态在session中
        session['user_username'] = username
        return jsonify(msg='登录成功', code=200, username=username)
    else:
        return jsonify(msg="账号或密码错误", code=4001)


# 检查用户登录状态
@user.route("/session", methods=["GET"])
def user_check_session():
    username = session.get("user_username")
    if username is not None:
        # 操作逻辑 数据库什么的
        # 数据库里面 把你的头像 等级 金币数量 查询出来
        return jsonify(username=username, code=200)
    else:
        return jsonify(msg="出错了，没登录")


# 用户登出
@user.route("/logout", methods=["DELETE"])
def user_logout():
    username = session['user_username']
    if username is None:
        return jsonify(msg='出错了，没有登录', code=4000)
    session.clear()
    return jsonify(msg="成功退出登录!", code=200)


# 用户成功响应
@admin.route('/index', methods=['GET'])
def hello_world():
    return 'Hello Cory! 这里是管理员响应！！'


# 管理员注册
@admin.route('/register', methods=['POST'])
def admin_register():
    try:
        my_json = request.get_json()
        print(my_json)
        username = my_json.get("username")
        password = my_json.get("password")
        if not all([username, password]):
            return jsonify(code='4000', msg='参数不完整')
        user = Admin(username=username, password=password)
        # 添加到数据库
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(code=200, msg='注册成功', username=username)
        except Exception as e:
            print(e)
            return jsonify(msg=e, code=4001)
    except Exception as e:
        print(e)
        return jsonify(msg='存数据失败', code=4001)


# 管理员登录
@admin.route("/login", methods=["POST"])
def admin_login():
    get_data = request.get_json()
    print(get_data)
    username = get_data.get("username")
    password = get_data.get("password")
    if not all([username, password]):
        return jsonify(msg="参数不完整")
    user = Admin.query.filter_by(username=username).first()
    if user and user.password == password:
        # 如果验证通过 保存登录状态在session中
        session['admin_username'] = username
        return jsonify(msg='登录成功', code=200, username=username)
    else:
        return jsonify(msg="账号或密码错误", code=4001)


# 检查管理员登录状态
@admin.route("/session", methods=["GET"])
def admin_check_session():
    username = session.get("admin_username")
    if username is not None:
        # 操作逻辑 数据库什么的
        # 数据库里面 把你的头像 等级 金币数量 查询出来
        return jsonify(username=username, code=200)
    else:
        return jsonify(msg="出错了，没登录")


# 管理员登出
@admin.route("/logout", methods=["DELETE"])
def admin_logout():
    username = session['admin_username']
    if username is None:
        return jsonify(msg='出错了，没有登录', code=4000)
    session.clear()
    return jsonify(msg="成功退出登录!", code=200)
