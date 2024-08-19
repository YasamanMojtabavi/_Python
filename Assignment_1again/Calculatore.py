import math

print("😊😊 Welcom to my Calculator: 😊😊")

for i in range(20):
    print("please enter your choice:")
    print("+ : sum")
    print("- : sub")
    print("* : mult")
    print("/ : div")
    print("sin")
    print("cos")
    print("cot")
    print("tan")
    print("factorial")
    print("sqrt")
    print("log")
    print("exit")
    op=input()
    
    if op == "exit":
        print("Thank you.")
        break

    if op =="+" or op=="-" or op =="*" or op =="/":
        a=float(input("enter first number:"))
        b=float(input("enter second number:"))
    else:
        a=float(input("enter number:"))
        
    if op == "+":
        result=a+b

    if op == "-":
        result=a-b

    elif op == "/":
        if b == 0:
            result="cannot divice by zero."
        else:
            result=a/b

    elif op =="*":
        result=a*b

    elif op == "sin":
        a=a*(math.pi/180)
        result=math.sin(a)

    elif op == "cos":
        a=a*(math.pi/180)
        result=math.cos(a)

    elif op == "tan":
        a=a*(math.pi/180)
        result=math.tan(a)

    elif op == "cot":
        a=a*(math.pi/180)
        result=math.cot(a)

    elif op == "factorial":
        result=math.factorial(a)

    elif op == "sqrt":
        result=math.sqrt(a)

    elif op == "log":
        result=math.log(a)

    print(result)
