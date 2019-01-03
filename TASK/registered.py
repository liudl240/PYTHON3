#!/usr/bin/env python3
import redis
import sys
import getpass

redis_connect=redis.Redis(host='localhost', port=6379, db=2,password=123456)
info="""++++++++++registered++++++++++++"""
welcome="""++++++++++welcome{_username}++++++++++++"""

username=input("input your your name :")
res=redis_connect.get('user_login_{_username}'.format(_username=username))
if res:
    print ("该%s用户已经存在"%(username))
    sys.exit(10)
else:
    count = 0
    while count  < 3:
        passwd1=getpass.getpass("input your passwd:")
        passwd2=getpass.getpass("input your passwd:")
        if passwd1 == passwd2:
            print("正在注册用户{_username}".format(_username=username))
            redis_connect.set('user_login_{_username}'.format(_username=username),'{_passwd}'.format(_passwd=passwd1))
            print("注册成功")
            print(welcome.format(_username=username))
            res=redis_connect.get('user_login_{_username}'.format(_username=username))
            print(res)
            sys.exit(0)
        else:
            print("上次密码输入不一致!!!")
            count+=1
    else:
        print ("输入密码错误次数过多...,请稍后再试!!!")
   
"""
    redis_connect.set('user_login_{username}'.format(_username=username),{_passwd}.format(_passwd=passwd))
print (res)
"""
