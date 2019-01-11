#!/usr/bin/env python3
#james liu

"""
集合
01 唯一的
02 无须的
"""


info=["james","james","liu","name"]
print(info)
print(set(info))


##set.clear 清空集合里的所有元素
set1=set(info)
set1.clear()
print(set1)

#set.pop  随机删除集合中的一个元素
set2=set(info)
print(set2)
set2.pop()
print(set2)

#set.copy  浅拷贝集合
set3=set(info)
set4=set3.copy()
print(set3)
print(set4)

#set.add  增加一个元素
set5=set(info)
set5.add("abc")
print(set5)
## set.update 增加一个集合
setgg={"ab","ac","james"}
set5.update(setgg)
print(set5)
print("this is test".center(50,"#"))

#set.remove set.discard 移除一个元素
#remove 不存在的元素会报错，而discard不会
set6=set5.copy()
print(set6)
set6.remove("abc")
print(set6)
set6.discard("james")
print(set6)

# len 计算set 长度
set7=set(info)
print(set7)
print(len(set7))

# in 判断是否在集合里面
set8=set(info)
print(set8)
if "james" in set8:
    print ("yes")
else:
    print("NO")

####两个集合之间的关系操作

# 并集
seta=("a","b","c")
setb=("1","2","3")
print (seta + setb)
# 集合a或b中包含的所有元素
seta=("a","b","c","1")
setb=("b","a")

#

"""
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
"""
