from flask import Blueprint
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)
# 创建蓝图对象
admin = Blueprint("admin", __name__)
from flask_project.caiji_blog.admin import api

