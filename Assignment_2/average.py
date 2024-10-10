average=0
sum=0
i=0
while True:
 choice=input("Hello, choose between two options, enter the number or exit?")
 
 if choice == "exit":
    break
 else:
    i=i+1
    choice=float(choice)
    sum=choice+sum
    average=sum/i
print(average)
