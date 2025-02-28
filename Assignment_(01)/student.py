name=input("pleas enter you'r name:")
family=input("pleas enter you'r family:")
number1=float(input("enter your number1:"))
number2=float(input("enter your number2:"))
number3=float(input("enter your number3:"))

average=(number1+number2+number3)/3

if average>=17:
     print("you'r status:graet")

elif average>=12:
     print("you'r status:normal")
     
elif average<12:
    print("you'r status:fail")
