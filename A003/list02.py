#!/bin/bash
#append 增
list1=["a","b","c","d"]
print(list1)
list1.append("james.liu")
print(list1)
#clear #清除
list1=["a","b","c","d"]
print(list1)

list1.clear()
print(list1)
#copy

list1=["a","b","c","d"]
print(list1)

list2=list1.copy()
print(list2)

list1=["a","b","c","d",["1","2","3"]]
list2=list1.copy()

list1[2]="james.liu"
list1[-1][2]="james"

print(list1)
print(list2)

# acount 
list1=["a","b","c","d"]
print(list1.count("a"))

list1.append("a")
print(list1.count("a"))

#index 

list1=["a","b","c","d"]
print(list1)
print(list1.index("b"))

list1.append("b")
print(list1)
print(list1.index("b"))

#insert
list1=["a","b","c","d"]
print(list1)


list1.insert(3,"zhangsan")
print(list1)

#pop
list1=["a","b","c","d"]
print(list1)

list1.pop()
print(list1)
#remove

list1=["a","b","c","d"]
print(list1)

list1.remove("a")
print(list1)

#reverse
list1=["a","b","c","d","##","12","4","A"]
print(list1)

list1.reverse()
print(list1)
#sort
list1=["a","b","c","d","##","12","4","A"]
print(list1)

list1.sort()
print(list1)
#extend


list1=["a","b","c","d"]
list2=["1","2"]
print(list1)
print(list2)

list1.extend(list2)
print(list1)
print(list2)

#改
list1=["a","b","c","d","##","12","4","A"]
print(list1)

list1[1]="james.liu"
print(list1)


list1=["a","b","c","d","##","12","4","A"]

print(list1[:])
print(list1[:3])
print(list1[-2:])
print(list1[2:5])
