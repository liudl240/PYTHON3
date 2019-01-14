#/usr/bin/env python3
#james.liu

"""
#装饰器的使用，通过高阶函数，不修改函数源代码，不修改函数的调用方式新增功能
第一个案例，引入修饰符@
    @就相当于test1=aa(test1)
第二个案例，函数带参数传入装饰器
第三个案例，装饰器带参数
"""
import sys
"################"
def aa(func):
    def demo():
        func()
        print("this is ok")
        print("这是第一个实例结束符".center(50,"#"))
    return  demo

def test0():
    print("hi,james liu")
test0=aa(test0)
test0()
"""
对比上面和下面的案例，这就是装饰器的使用
"""

@aa
def test1():
    print("hi,james liu")

test1()
"################"

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
        func(*args,**kwargs)
        print("this is ok")
        print("这是第三个实例结束符".center(50, "#"))
    return demo
@cc
def test3(name,age):
    info="name:%s,age:%d" %(name,age)
    print(info)

test3("james",23)

"################"

def auth(type):
    def indomo(func):
        if type == "ldap":
            def domo(*args, **kwargs):
                input_username = input("input your username:")
                input_passwd = input("input your  passwd:")
                username = "james"
                passwd = "james"
                if username == input_username and passwd == input_passwd:
                    res=func(*args,**kwargs)
                    print("\033[31mwelcome %s \033[0m".center(50,"#")%(username))
                    return res
                else:
                     print("输入用户名密码错误")
                     sys.exit(10)
        elif type == "sys":
            def domo(*args, **kwargs):
                input_username = input("input your username:")
                input_passwd = input("input your  passwd:")
                username = "james"
                passwd = "james"
                if username == input_username and passwd == input_passwd:
                    res=func(*args,**kwargs)
                    print("\033[31mwelcome %s \033[0m".center(50,"#")%(username))
                    return res
                else:
                     print("输入用户名密码错误")
                     sys.exit(10)
        return domo
    return indomo


def index_pages():
    print("this is index pages".center(50,"#"))

@auth(type="sys")
def home(username):
    print("this is home pages".center(50,"&"))
    return "this is %s home".center(50,"!") %(username)
@auth(type="ldap")
def blog():
    print("this is blog pages".center(50,"@"))


index_pages()
print(home("kebe"))
blog()
