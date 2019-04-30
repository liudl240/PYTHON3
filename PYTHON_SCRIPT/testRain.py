#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : James liu
# * Email         : ybooks.liu@gmail.com
# * Create time   : 2019-04-29 02:14
# * Last modified : 2019-04-29 02:14
# * Filename      : testRain.py
# * Description   : 随机判断是否下雨并且是否外出 
# **********************************************************
import random
import time

#单数为下雨
#大于10表示有伞

while True:
    num=random.randint(1,20)
    print(num)
    if int(num) % 2:
        print("现在没有下雨，我要出去咯")
        break
    else:
        print("现在下雨咯，我去找找伞") 
        if int(num) > 10:
            print("虽然下雨了，但是我有伞，我可以出去")
            break
        else:
            print("我出不去了，我没有伞，我需要再等等雨有没有停")
            time.sleep(2)
            continue

print("外面真的漂亮")
