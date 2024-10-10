i=1
sum=0
while True:
    number=input("please enter number : ")

    if number=="exit":
        break
    else:
        number=float(number)
        sum=sum+number
        average=sum/i
        i=i+1

print("student average = ", average)