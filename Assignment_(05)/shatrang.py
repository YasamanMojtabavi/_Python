def shatrangg(n,m):
    for i in range(n):
        for j in range(0,m):
             if ((i+j)%2)==0 :
              print("⬛",end="")
             else:
              print("⬜",end="")
        print()   
           
N=int(input("please enter N:"))
M=int(input("please enter M:"))