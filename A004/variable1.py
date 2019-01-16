"""
局部变量和全局变量
"""
"""
username 和 age 是全局变量
cell_phone是局部变量
phone_type 通过global转为全局变量
"""
username="james.liu"
age="23"

def info():
    cell_phone="123456789"
    global phone_type
    phone_type = "华为"
    print("{_age}岁的{_username}的电话号码是{_cell_phone},手机类型是{_phone_type}".format(_username=username,_age=age,_cell_phone=cell_phone,_phone_type=phone_type))
    return 0

info()
try:
    print("phone_type 通过global,转为全局变量",phone_type)
    print("{_age}岁的{_username}的电话号码是{_cell_phone},手机类型是{_phone_type}".format(_username=username,_age=age,_cell_phone=cell_phone,_phone_type=phone_type))
except NameError as reson:
    print("cell_phone是局部变量，这里无法显示",reson)

