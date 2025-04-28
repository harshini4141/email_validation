#a-z  hars@gmail.com
#0-9
#. _ time1
#@ time 1
#.2,3
#by using regex module
import re
email_condition="^[a-z]+[\._|]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter you r email:")
if re.search(email_condition,user_email):
    print("right email")
else:
    print("wrong email")    