#nested if and elif else
n=int(input("enter a number"))
if n%3==0:
    if n%4==0 and n%5==0:
        print(n,"is divisible by 3,4 and 5")
    elif n%5==0:
        print(n,"is divisible 3 and 5")
    elif n%4==0:
        print(n,"is divisible by 3 and 4")    
    else:
        print(n,"is divisible by only 3")
else:
    if n%4==0:
        if n%5==0:
            print(n,"divisible by 4 and 5")
        else:
            print(n,"divisible by only 4")
    elif n%5==0:
         print(n,"divisible by 5")
    else:
        print(n,"is not divisible by 3,4,5 ")    
        # assignment....accept a number check whether the number id divisible by 3,4.  
      
                         