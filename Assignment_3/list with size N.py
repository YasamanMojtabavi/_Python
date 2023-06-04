import random
N=int(input("please enter number: "))
list_N=[]

while (len(list_N)) != N:
    number=random.randint(0,100)
    if number not in list_N:
       list_N.append(number)

print(list_N)