import getpass
"""
输入用户名密码
"""
name = input("name :")
passwd = int(input("passwd :"))

info ="""++++++++++++++++info {_name}+++++++++++++++++
name={_name}
passwd={_passwd}
""".format(_name=name,
           _passwd=passwd)
print(type(name))
print()

