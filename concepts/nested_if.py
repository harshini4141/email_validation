#nested if....accept student inter marks and eamcet marks check whether the student id eligible to b-Tech or degree
inter=int(input("enter the inter marks"))
EAMCET=int(input("enter the EAMCET marks"))
if inter>=240:
    if EAMCET>=40:
        print("eligible to B.tech")
    else:
        print("join in degree")
else:
    print("go and write supply")            
