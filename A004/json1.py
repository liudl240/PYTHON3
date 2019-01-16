"""
导入json
"""
import json
"""
生产字典
"""
list1={
    "name":"james.liu",
    "age":"23",
    "salay":"1500"
}
"""
将字典写入到文本中
"""
with open("./json.txt","w") as f:
    f.write(json.dumps(list1))
    f.close()
"""
读取文本，
"""
with open("./json.txt","r") as f:
    print(json.loads(f.read())["age"])
    f.close()
