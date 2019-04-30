#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : James liu
# * Email         : ybooks.liu@gmail.com
# * Create time   : 2019-04-29 05:38
# * Last modified : 2019-04-29 05:38
# * Filename      : inputYourName.py
# * Description   : 
# **********************************************************
nameList = []
while True:
    newName = input("请输入你的名字:")
    if newName == '':
        break
    nameList = nameList + [newName]
    continue

print(len(nameList))
for i in nameList:
    print(i)
