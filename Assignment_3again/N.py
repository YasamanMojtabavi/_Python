import random
n=int(input("please enter N: "))
N=[]
for i in range(n):
    number=random.randint(0,1000)
    while number in N:
        number=random.randint(0,1000)
    N.append(number)

print(N)

