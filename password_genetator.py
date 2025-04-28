import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="~!@#$%^&*()_+=-[]{};:',.<>?/|`"
all_chars=lower+upper+numbers+symbols
length=int(input("enter the length of a password:"))
password=" ".join(random.sample(all_chars,length))
print("generated password:",password)