print("please enter numbers to draw a triangle:")
a=float(input("number1:"))
b=float(input("number2:"))
c=float(input("number3:"))

if a+b>c and a+c>b and b+c>a:
    print("you can draw triangle.")
else:
    print("you cannot draw.")
