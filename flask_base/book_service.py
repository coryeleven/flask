# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 6:12 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : books_service.py
# @Software : PyCharm
from book_model import db, Author, Book

# db.drop_all()
db.create_all()


def put_author():
    author = Author(name='张三')
    db.session.add(author)
    db.session.commit()


def put_books():
    book = Book(name='学渣养成记', author_id='author.id')


if __name__ == '__main__':
    put_author()
