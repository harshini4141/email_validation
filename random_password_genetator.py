import random
#get the desired password length from the user
passlen=int(input("Enter the length of the password:"))

#define the character set for the password
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=[]{}/.,;'<>:|\?`~`"

#generate the password by sampling characcters from 's'
p="".join(random.sample(s,passlen))

#print the generated password
print("generated password:",p)