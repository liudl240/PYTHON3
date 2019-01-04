#_coding:utf-8
alist=["a","b","c","d","e","f","g"]

#打印列表
print(alist[:])
print(alist)

#列表切割

print(alist[1])

print(alist[:2])

print(alist[-2:-1])
print(alist[-2:])

##获取索引
print(alist.index("b"))
##统计
print(alist.count("b"))
##apend
alist.append("james")
print(alist)
##insert
alist.insert(2,"liu")
print(alist)
##改
alist[2]="james.liu"
print(alist)
##删除
del alist[2]
print(alist)
alist.remove("a")
print(alist)
alist.pop()
print(alist)
##拷贝
alist1=alist.copy()
print(alist1)
alist2=alist[:]
print(alist2)
alist=["a","b","c","d","e","f","g",["1","2","3"]]
print(alist)

