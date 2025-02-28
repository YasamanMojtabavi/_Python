number_1=int(input("enter number1 : "))
number_2=int(input("enter number2 : "))

if number_1 != 0 and number_2 != 0:
    if abs(number_1)>abs(number_2):
        n=abs(number_2)
    else:
        n=abs(number_1)

    for i in range(n,0,-1):
        if abs(number_1)%i== 0 and abs(number_2)%i== 0:
            Bmm=i
            break
else:
   Bmm=0     

print("BMM: ",Bmm)     

 

