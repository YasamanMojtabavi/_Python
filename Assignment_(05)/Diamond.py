def diamooond(n):    
    for i in range(n):
        h=n-i+2
        while h>2:
         print(" ",end="")
         h=h-1
        for j in range(i*2+1):
             print("*",end="")
        print()
    for i in range(n-1,0,-1):
        h=n-i+1
        while h>0:
         print(" ",end="")
         h=h-1
        for j in range((i-1)*2+1,0,-1):
         print("*",end="")
        print()   

n=int(input("Enter N:"))
diamooond(n)