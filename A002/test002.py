import sys
"""
猜猜大小
"""
#coding:utf8
james_age=18
#abc=[1,2,3]
#for i in abc:
count=0
while count < 3 :
    age=int(input("input age of james :"))
    if age == james_age:
        print ("你猜对了")
        sys.exit(0)
    elif age > james_age:
        print("你猜大了")
    elif age < james_age:
        print ("你猜小了")
    count+=1
    if count == 3:
        result=input("你是否需要继续玩？：【y|n】")
        if result == "y":
            count = 0
else:
    print ("你已经没有次数去试了!!!")
print ("试了三次结束!!!,james年龄是",james_age)
print ("试了三次结束!!!,james年龄是{_james_name}".format(_james_name=james_age))
print ("试了三次结束!!!,james年龄是%s" %(james_age))