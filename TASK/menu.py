#!/usr/bin/env python3
import sys
list1=[["a1","a2","a3","a4"],["b1","b2","b3","b4"],["c1","c2","c3","c4"]]
while True:
    choose1=input("输入0,1,2,q退出:")
    if choose1 == "q":
        sys.exit(0) 
    elif int(choose1) >= 3:
        print ("没有该{_choose1}选项".format(_choose1=choose1))
        sys.exit(0) 
    else:
       for i in list1[int(choose1)]:
           print (i) 
