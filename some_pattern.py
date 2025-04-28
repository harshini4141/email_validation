# n=8
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1 or (i==j and j< n//2) or (i+j==n-1 and j>= n//2)):
#             print("h",end=" ")
#         else:
#             print(" ",end=" ")
#     print()       
    
# n=9
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1 or i==n//2):  # Changed condition to create H pattern
#             print("h",end=" ")
#         else:
#             print(" ",end=" ")
#     print()   
    
# n=9
# for i in range(n):
#     for j in range(n):
#         if(j==0 or (j==n-1 and i<=n//2) or i==0 or i==n//2 or (i==j and i>=n//2)):
#             print("r",end=" ")
#         else:
#             print(" ",end=" ")
#     print()     
# n=8
# for i in range(n):
#     for j in range(n):
#       if(j==0 or (j==n-1 and i==n//2) or (i==0 or i==n//2)):
#         print("b",end=" ")
#     else:
#         print(" ",end="")  
# n=8
# for i in range(n):
#     for j in range(n):
#         if(j==0 or (j==n-1 and (i!=0 and i!=n-1)) or (i==0 or i==n-1 or i==n//2)):
#             print("b",end=" ")
#         else:
#             print(" ",end=" ")
#     print()  
# n=9
# for i in range(n):
#     for j in range(n):
#         if(j==0 or(i==0 or i==n//2)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()       

n=9
for i in range(n):
    for j in range(n):
        if j==n//2 or (i==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
    
                   
