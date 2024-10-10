number_1=int(input("enter number1 : "))
number_2=int(input("enter number2 : "))
j=abs(number_1 *number_2)+1

if number_1 != 0 and number_2 != 0:
    if abs(number_1)>abs(number_2):
            n=abs(number_1)
    else:
            n=abs(number_2)

    for i in range(n,j):
        if i%abs(number_1)== 0 and i%abs(number_2)== 0:
            Kmm=i
            break
else:
      if number_2 !=0:
            Kmm=number_2
      else:
            Kmm=number_1     
print("kMM: ", Kmm) 