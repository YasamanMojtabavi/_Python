def rhombu(o):
    j=o
    i=1
    for l in range(o+1):
        while j>=-1 and i<=(2*o-1):
            for n in range (j):
             print(" ",end="")
            for m in range(i):
                print("*",end="")
            j=j-1 
            i=i+2
            print()
    
    for l in range(o+1):
        while j<=o and i>=-2:
            for n in range (j):
             print(" ",end="")
            for m in range(i):
                print("*",end="")
            j=j+1 
            i=i-2
            print()       
    
o=int(input("Hello,please enter n: "))
rhombu(o)