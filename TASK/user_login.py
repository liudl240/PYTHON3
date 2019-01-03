#!/usr/bin/env python3
import redis
import sys
import getpass
redis_connect=redis.Redis(host='localhost', port=6379, db=2,password=123456)
redis_connect1=redis.Redis(host='localhost', port=6379, db=3,password=123456)
info="++++++++++++LOGIN+++++++++++++++"

def expire_time(username):
    redis_connect1.set('user_login_expire_{_username}'.format(_username=username),1)
    redis_connect1.expire('user_login_expire_{_username}'.format(_username=username),300)
def expire_over_time(username):
    over_time=int(redis_connect1.ttl('user_login_expire_{_username}'.format(_username=username)))
    return over_time
    
    


count = 0
while count < 3:
    print(info)
    username=input("pleace,input your username:") 
    res_username = redis_connect.get('user_login_{_username}'.format(_username=username))
    if res_username:
        over_time=expire_over_time(username)
        if over_time > 0 :
            print("此{_username}还需要{_over_time}S时间解锁!!!".format(_username=username,_over_time=over_time))
            sys.exit(0)
        else:
            passwda=str(res_username)
            passwdb=passwda.split("'",2)[1]
            falsecount=0
            while falsecount < 3:
                passwd_input=getpass.getpass("请输入密码:")
                if passwd_input == passwdb:
                    welcome="++++++++++++WELCOME {_username}+++++++++++++++".format(_username=username)
                    print (welcome)
                    sys.exit(0)
                else:
                    falsecount+=1
                    print("输入密码错误")
                    continue
            else:
                expire_time(username)
                print("输入密码失败次数过多，冻结五分钟")
                sys.exit(5)
    else:
        print ("没有%s该用户"%(username))
        sys.exit(100)
    passwd=getpass.getpass("pleace,input your passwd:") 
else:
    print ("{username}输入密码次数过多，封锁五分钟!!!".format(_username=username))
    sys.exit(0)

