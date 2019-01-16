import pickle
list1={
    "name":"james.liu",
    "age":"23",
    "salay":"1500"
}

print(pickle.dumps(list1))
with open("./json.txt","wb") as f:
    f.write(pickle.dumps(list1))
    f.close()


with open("./json.txt","rb") as f:
    print(pickle.loads(f.read())["age"])
    f.close()
