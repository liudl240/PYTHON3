"""
列表生成器
"""
list1=[i for i in range(10)]

for i in list1:
    print(i)

generator1=(i for i in range(10))
print(generator1)

print(generator1.__next__())
print(generator1.__next__())

"""
生产器
函数
yield
"""
print("#"* 50)
def fbnq(count):
    num=0
    a=1
    b=1
    if count==1:
       yield (a)
    elif count==2:
        yield (b)
    else:
        while   num < count:
            num +=1
            a,b = b,a+b
            yield (b)
#        return "done"
res=fbnq(4)
print(res.__next__())
print(res.__next__())
print(res.__next__())


"""
生产器
函数
"""
def fbnq1(count):
    num=0
    a=1
    b=1
    if count==1:
       yield (a)
    elif count==2:
        yield (b)
    else:
        while   num < count:
            num +=1
            a,b = b,a+b
            yield (b)

res=fbnq1(100)
while True:
    try:
        print(next(res))
    except StopIteration as reson:
        print(reson)
        break
