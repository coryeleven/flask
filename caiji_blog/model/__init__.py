# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 12:50 上午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
import sys, os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
"""
print(__file__)  # 当前执行的文件名
print(os.path.abspath(__file__))  # 当前执行的文件路径
print(os.path.dirname(os.path.abspath(__file__)))  # 当前执行的上级文件路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 当前执行上上级的文件路径
"""
