# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 2:03 上午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
# from pk1.class1 import classOne
# from pk2.class2 import classTwo
#
# if __name__ == "__main__":
#     c1 = classOne()
#     c1.printInfo()
#     c2 = classTwo()
#     c2.printInfo()

# 运行结果：
# i am class One!
# i am class two!

import pk2
import pk1

if __name__ == "__main__":
    c1 = pk1.classOne()
    c1.printInfo()
    c2 = pk2.classTwo()
    c2.printInfo()

# 运行结果：
# i am class One!
# i am class two!