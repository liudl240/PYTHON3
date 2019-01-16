list1={
    "name":"james.liu",
    "age":"23",
    "salay":"1500"
}
data=str(list1)
with open("./json.txt" ,"w") as f:
    f.write(data)
    f.close()


"""
通过eval转化文字为字典
"""
with open("./json.txt","r") as f:
    data=eval(f.read())
    print(data["name"])

