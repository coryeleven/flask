from flask import Blueprint

# 创建蓝图对象
main = Blueprint("main", __name__)

from flask_project.caiji_blog.main import api
