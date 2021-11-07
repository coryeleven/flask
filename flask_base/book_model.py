# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 6:31 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : book_model.py
# @Software : PyCharm
from flask_project import Flask, render_template, flash, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required
from flask_wtf import FlaskForm

app = Flask(__name__)
# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@cory.net.cn:3306/ops'
# 跟踪数据库修改,不建议修改
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'tetxtxtaskgd'
"""
_sqlalchemy 中默认使用 MySQLdb 连接数据库
而这个包仅支持py2语法，所以要单独安装 pymysql 并使用它作为flask_sqlalchemy连接的内核。
"""
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


# 作者模型
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    # 关系引用，books是给自己（Authors模型）用的，authors 是给Book模型使用的
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author: %s' % self.name


# 书籍模型
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return 'Books: %s %s' % (self.name, self.author_id)


# 自定义表单类
class AuthForm(FlaskForm):
    author = StringField('作者', validators=[data_required()])
    book = StringField('书籍', validators=[data_required()])
    submit = SubmitField('提交')


@app.route('/index', methods=['GET', 'POST'])
def get_index():
    # 创建自定义表单类
    auth_form = AuthForm()
    # 查询所有作者信息
    authors = Author.query.all()
    return render_template('books.html', authors=authors, form=auth_form)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建自定义表单类
    auth_form = AuthForm()
    if auth_form.validate_on_submit():
        author_name = auth_form.author.data
        book_name = auth_form.book.data
        author = Author.query.filter_by(name=author_name).first()
        if author:
            book = Book.query.filter_by(name=book_name).first()
            if book:
                flash('已存在同名书籍')
            else:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print('添加书籍失败！', e)
                    flash(e)
        else:
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()

            except Exception as e:
                print(e)
                flash('添加作者和书籍失败！')
                db.session.rollback()
    else:
        if request.method == 'POST':
            flash('参数不全')
    # 查询所有作者信息
    authors = Author.query.all()
    return render_template('books.html', authors=authors, form=auth_form)


# 删除书籍
@app.route('/delete/<book_id>')
def delete_book(book_id):
    print(book_id)
    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍失败')
            db.session.rollback()
    else:
        flash('书籍未找到，删除失败')
    return redirect('http://127.0.0.1:8080')
    # return redirect(url_for('index'))


# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    print(author_id)
    author = Author.query.get(author_id)
    if author:
        try:
            Book.query.filter_by(author_id=author.id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者书籍失败')
            db.session.rollback()
    else:
        flash('作者未找到，删除失败')
    return redirect('http://127.0.0.1:8080')
    # return redirect(url_for('index'))


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au1 = Author(name='老王')
    # au2 = Author(name='老六')
    # au3 = Author(name='老三')
    # au4 = Author(name='老四')
    # au5 = Author(name='老五')
    # db.session.add_all([au1, au2, au3, au4, au5])
    # db.session.commit()
    # bk1 = Book(name='水浒传', author_id=au1.id)
    # bk2 = Book(name='西游记', author_id=au2.id)
    # bk3 = Book(name='斑马', author_id=au3.id)
    # bk4 = Book(name='河马', author_id=au5.id)
    # bk5 = Book(name='山羊', author_id=au1.id)
    # bk6 = Book(name='大象', author_id=au4.id)
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6])
    # db.session.commit()
    app.run(debug=True, port=8080)
