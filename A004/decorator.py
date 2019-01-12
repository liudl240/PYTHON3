#/usr/bin/env python3
#james.liu

"""
#装饰器的使用，通过高阶函数，不修改函数源代码，不修改函数的调用方式新增功能
第一个案例，引入修饰符@
    @就相当于test1=aa(test1)
第二个案例，使用修饰符
第三个案例，如何传参数
第四个案例，
"""

def aa(func):
    def demo():
        func()
        print("this is ok")
        print("这是第一个实例结束符".center(50,"#"))
    return  demo

def test1():
    print("hi,james liu")
test1=aa(test1)
test1()


def bb(func):
    def demo():
        func()
        print("this is ok")
        print("这是第二个实例结束符".center(50, "#"))
    return demo

@bb
def test2():
    print("hi ,james")

test2()

def cc(func):
    def demo(*args,**kwargs):
        res=func(*args,**kwargs)
        print("this is ok")
        print("这是第三个实例结束符".center(50, "#"))
        return  res
    return demo
@cc
def test3(name,age):
    info="name:%s,age:%d" %(name,age)
    print(info)
    return  "this is return"

print(test3("james",23))
