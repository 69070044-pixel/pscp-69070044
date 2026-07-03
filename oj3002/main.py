"""OJ3002"""
uname = input()
sname = input()
user_age = input()

if len(uname) >= 5 and len(sname) >= 5:
    pwd = uname[:2] + sname[-1] + user_age[-1]
else:
    pwd = uname[0] + user_age + sname[-1]
print(pwd)
