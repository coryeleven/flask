# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 2:52 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : create_User.py
# @Software : PyCharm
from model import db, User, Role


def init_db():
    db.drop_all()
    db.create_all()


def put_role():
    role = Role(username='admin')
    db.session.add(role)
    user1 = User(name='张三', email='zs@email.com', password='111111', role_id=role.id)
    user2 = User(name='李四', email='ls@email.com', password='111111', role_id=role.id)
    user3 = User(name='小三', email='xs@email.com', password='111111', role_id=role.id)
    user4 = User(name='小四', email='xss@email.com', password='111111', role_id=role.id)
    user5 = User(name='小五', email='xw@email.com', password='111111', role_id=role.id)
    user6 = User(name='小六', email='xl@email.com', password='111111', role_id=role.id)
    user7 = User(name='小七', email='xq@email.com', password='111111', role_id=role.id)
    user8 = User(name='小八', email='xb@email.com', password='111111', role_id=role.id)
    user9 = User(name='小九', email='xj@email.com', password='111111', role_id=role.id)
    db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9])
    db.session.commit()


def query_all():
    return User.query.all()


if __name__ == '__main__':
    print(query_all())
    print(User.query.all())
    # filter_by: 属性=
    # filter: 对象.属性==,功能更强大哦，可以实现更多的一些查询，支持比较运算符
    print(User.query.filter_by(id=4).first(),
          User.query.first(),
          User.query.count(),
          User.query.all(),
          User.query.filter(User.id == 1).first())
