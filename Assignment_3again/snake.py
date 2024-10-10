N=int(input("please enter N :"))
for i in range(N):
    if i%2 == 0:
        print("*",end="")
    else:
        print("#",end="")