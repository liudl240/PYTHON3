#!/usr/bin/python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : James liu
# * Email         : ybooks.liu@gmail.com
# * Create time   : 2019-04-29 21:34
# * Last modified : 2019-04-29 21:34
# * Filename      : pyperclipTest.py
# * Description   : 
# **********************************************************
import pyperclip
import sys
import json

accoutFile = "./passwd"
PASSWORDS = dict()
def accoutDict(accoutFile):
    with open(accoutFile, 'r') as usersFile:
        for i in usersFile.readlines():
            test = json.loads(i)
            PASSWORDS.update(test)
        return PASSWORDS
        usersFile.close()
    return PASSWORDS

def addUser(PASSWORDS, accoutFile):
    for i in range(3):
        USER = input("请输入你的用户名:")
        if USER not in PASSWORDS:
            PW = input("请输入你的密码:")
            if PW != '': 
                PW2 = input("请再次输入你的密码:")
                if PW == PW2: 
                    description = input("请输入该账号作用:")
                    PASSWORDS[USER] = [PW, description]
                    with open(accoutFile, 'w') as passwdFile:
                        json.dump(PASSWORDS, passwdFile, ensure_ascii=False)
                        passwdFile.write('\n')
                        passwdFile.close()
                    print("用户名密码已经存储..")
                    break
                else:
                    print("两次输入的密码不一致:")
                    continue
            else:
                print("输入密码为空,无法完成登记!!")
                continue
        else:
            print("该用户已存在,无法添加,正在退出...")
            continue
    return 

def modifyPasswd(PASSWORDS, accoutFile):
    for num in range(3):
        USER = input("请输入你的用户名:")
        if USER in PASSWORDS:
            PW = input("第一次输入密码:")
            if PW != '':
                PW2 = input("第二次输入密码:")
                if PW == PW2:
                    PASSWORDS[USER][0] = PW
                    with open(accoutFile, 'w') as passwdFile:
                        json.dump(PASSWORDS, passwdFile, ensure_ascii=False)
                        passwdFile.write('\n')
                        passwdFile.close()
                        print(USER+"用户密码修改完成...")
                        break
                else:
                    print("两次输入的密码不一致:")
                    continue
            else:
                print("输入你的密码为空")
                continue
        else:
            print(USER + "该用户不存在!!!")
            continue
def delUser(PASSWORDS, accoutFile):
    USER = input("请输入你需要删除的用户名：")
    if USER in PASSWORDS:
        del PASSWORDS[USER]
        with open(accoutFile, 'w') as passwdFile:
            json.dump(PASSWORDS, passwdFile, ensure_ascii=False)
            passwdFile.write('\n')
            passwdFile.close()
            print(USER+"用户移除完成...")
    else:
        print(USER+"用户不存在")

def checkUsers(PASSWORDS):
    for USER in PASSWORDS.keys():
        print(USER + "\t该账号作用: " + PASSWORDS[USER][1])

def copyPasswd(PASSWORDS):
    USER = input("请输入你需要拷贝的用户名:")
    if USER in PASSWORDS:
        pyperclip.copy(PASSWORDS[USER][0])
        print(USER + "用户的密码已经拷贝")
    else:
        print("用户名不存在")



def cmd():
    if len(sys.argv) < 2:
        print("请输入参数addUser |modifyPasswd|delUser|checkUsers|copyPasswd")
    elif sys.argv[1] == "addUser":
        addUser(accoutDict(accoutFile), accoutFile)
    elif sys.argv[1] == "modifyPasswd":
        modifyPasswd(accoutDict(accoutFile), accoutFile)
    elif sys.argv[1] == "delUser":
        delUser(accoutDict(accoutFile), accoutFile)
    elif sys.argv[1] == "checkUsers":
        checkUsers(accoutDict(accoutFile))
    elif sys.argv[1] == "copyPasswd":
        copyPasswd(accoutDict(accoutFile))
    else:
        print("输入参数有误:" + sys.argv[1])
        print("参数有：addUser |modifyPasswd|delUser|checkUsers|copyPasswd")

cmd()
#print(accoutDict(accoutFile))
#addUser(accoutDict(accoutFile), accoutFile)
#modifyPasswd(accoutDict(accoutFile), accoutFile)
#delUser(accoutDict(accoutFile), accoutFile)
#checkUsers(accoutDict(accoutFile))
#copyPasswd(accoutDict(accoutFile))
