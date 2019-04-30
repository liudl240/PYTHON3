#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : James liu
# * Email         : ybooks.liu@gmail.com
# * Create time   : 2019-04-29 03:36
# * Last modified : 2019-04-29 03:36
# * Filename      : defTest.py
# * Description   : 
# **********************************************************
def test(num1):
    num=int(num1)
    if num < 10:
        print(str(num) + "小于10")
    elif 20 >= num >= 10:
        print(str(num) + "大于等于10并小于等于20")
    else:
        print(str(num) + "大于20")
age=input("输入:")
test(age)
