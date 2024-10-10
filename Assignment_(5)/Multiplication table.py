def multiplication(n,m):
   
    print("x"," ",end="")
    for i in range(1,m+1):
        print(i," ",end="")
    print()
    sum=0
    for i in range(1,n+1):
        for j in range(1,m+1):
             if j==1:
                 sum+=1
                 print(sum," ",end="")
             print(i*j," ",end="")
        print()   

N=int(input("please enter N:"))
M=int(input("please enter M:"))
multiplication(N,M)