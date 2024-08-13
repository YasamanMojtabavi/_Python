n=int(input("Hello get me N :"))

first=0
second=1
number=1
for i in range(1,n+1):
    print(number)
    number=first+second
    first=second
    second=number
    
    