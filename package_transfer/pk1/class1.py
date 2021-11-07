# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 2:04 上午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# class classOne:
#     def __init__(self):
#         self.name = "class one"
#
#     def printInfo(self):
#         print("i am class One!")

# import os, sys
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 这里是把顶层目录加入到python的环境变量中。
# sys.path.append(BASE_DIR)
# print(BASE_DIR)
#
# # 路径要写完整
# from package_transfer.pk2.class2 import classTwo


class classOne:
    def __init__(self):
        self.name = "class one"

    def printInfo(self):
        print("i am class One!")


if __name__ == "__main__":
    c2 = classTwo()
    c2.printInfo()

# 运行结果：
# i am class two!
