"""
range
"""
james_age=18
for i in range(0,10,2):
    age=int(input("input james name:"))
    if age == i:
        print ("你猜对了!!!")
        break
    elif age > i:
        print ("你猜大了！！！")
    elif age < i:
        print ("你猜小了!!!")
print ("你已经试完了!!!,james年龄是{_james_age}".format(_james_age=james_age))