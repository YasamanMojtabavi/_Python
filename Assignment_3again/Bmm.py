number1=int(input("enter number1: "))
number2=int(input("enter number2: "))

num1=[]
mm=[]
bmm=0

for i in range(1,number1+1):
    if number1%i == 0 :
        num1.append(i)

for i in range(1,number2+1):
    if number2%i == 0 and i in num1:
        mm.append(i)

for i in range(0,len(mm)):
        if mm[i]>bmm:
            bmm=mm[i]

print("bmm=",bmm)