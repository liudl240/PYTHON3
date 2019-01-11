#!/usr/bin/env python3
#james liu
"""
字典的使用
01-字典是一个无序的，唯一的key=value 的类型对象
"""

#创建字典
dictionary1={'name':"james.liu",'age':'23'}

#查看字典
print(dictionary1["name"])
print(dictionary1)
print(dictionary1.items())
print(dictionary1.get('name'))
"""
区别
dictionary1.get(key) #key 不存在的时候return None
dictionary1[key] #key 不存在的时候报错
"""
print(dictionary1.get('salay'))
#print(dictionary1['salay'])




#增加
dict1=dictionary1.copy()
dict1["salay"]=15000
print(dict1.items())

#改
print(dictionary1)
dictionary1['name']="james"
print(dictionary1)


#删除
dictionary2=dictionary1.copy() #dictionary2=dictionary1会给clear清除
dictionary3=dictionary1.copy()
print(dictionary2.items())
dictionary2.clear() #清空dictionary2
print(dictionary2.items())
del dictionary1['name'] #删除
print(dictionary1)

print(dictionary3.items())
# dictionary3.pop("age")  #删除
print(dictionary3.items())



### 查看字典
print(dictionary1)
print(len(dictionary1))

###判断
info={'name':"james","age":'23',"salay":"15000"}
print(info)
if "james" in info["name"]:
    print("YES")
else:
    print("NO james")
## 字符串形式
print("this is test".center(50,"#"))
print(str(dict1))


########
#dict2=dict1.copy() #浅复制一个字典
##dict2.copy() ##浅复制一个字典
#dict2.get("name",delattr("james ok")) # 
#dict2.fromkeys()
#dict2.has_key(key)
#dict2.items()
#dict2.keys()
#dict2.setdefault()
#dict2.values()
#dict2.pop()
#dict2.items()
#dict2.clear()  #删除字典里的所有元素
