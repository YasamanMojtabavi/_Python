number1=int(input("enter number1: "))
number2=int(input("enter number2: "))

j=number1*number2+1
if number1>number2:
    for i in range(number2,j):
        if i%number1==0 and i%number2==0:
            kmm=i
            break
else:
    for i in range(number2,j):
        if i%number1==0 and i%number2==0:
            kmm=i
            break

print("kmm = ",kmm)
