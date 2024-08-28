def Ches(n,m):
    for i in range(n):
      print()
      for j in range(m): 
         if (i+j)%2==0:
            print("⬜",end="")
         else:
            print("⬛",end="")
    
n=int(input("Hello,please enter n: "))
m=int(input("please enter m: "))
Ches(n,m)