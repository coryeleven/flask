# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 9:18 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# @File    : app.py.py
# @Software : PyCharm

# 1.导入flask扩展
from flask import Flask, render_template, jsonify, request, flash

# 2.创建flask应用程序实例，需要传入__name__,作用是为了确定资源所在的路径
app = Flask(__name__)
app.secret_key = 'iteascsadasd'


# 3.定义路由，及视图函数
# Flask中定义路由是通过装饰器实现的
# 路由默认只支持GET
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'success'


# 路由传参，默认当作String处理，<int:order_Id>代表int类型
@app.route('/orders/<order_id>')
def get_order_id(order_id):
    return 'order_id  {}'.format(order_id)


# render_templates,返回一个网页（模版），第一个参数是模版的文件名，后面的参数都是键值对
@app.route('/render')
def get_render():
    url_str = 'www.baidu.com'
    url_json = {
        'name': 'name1',
        'phone': '110'
    }
    url_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    url_int = 100
    return render_template('index.html', url_str=url_str, url_json=url_json, url_list=url_list, url_int=url_int)


# 实现一个简单的登录逻辑
# 1.路由参数需要有GET,POST两种--》需要判断请求方式
# 2.获取请求的参数
# 3.判断参数是否都填写，密码是否相同
# 4.如果判断都没有问题，返回一个success
@app.route('/register', methods=['GET', 'POST'])
def register():
    # 判断发送client发送请求类型
    # 自己请求自己的逻辑中。GET只用来解析模板，而POST用来判断数据逻辑
    if request.method == "POST":
        # 使用form属性来接受表单提交过来的数据
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        # 判断数据是否同时存在
        if not all([username, password, password1]):
            flash('参数不足')
        elif password != password1:
            flash('两次密码不一致')
        else:
            flash('注册成功')
            # 将定义好的表单传递给模板，进行方法化设置
    return render_template('flask_register.html')


if __name__ == '__main__':
    # 4.启动程序
    app.run(debug=True)
