#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : James liu
# * Email         : ybooks.liu@gmail.com
# * Create time   : 2019-04-29 04:33
# * Last modified : 2019-04-29 04:33
# * Filename      : guestNumber.py
# * Description   : 
# **********************************************************
import random

def guestNumberGate():
    number = random.randint(1,100)
    while True:
        guestNumber = int(input("请输入你猜的数字:"))
        if number == guestNumber:
            print("\033[34m您太厉害了，恭喜您，猜对了！！！\033[0m")
            break
        elif number > guestNumber:
            print("差一点,"+"\033[31m你猜小了。\033[0m")
            continue
        elif number < guestNumber:
            print("差一点，"+"\033[32m你猜大了\033[0m")
            continue


guestNumberGate()
