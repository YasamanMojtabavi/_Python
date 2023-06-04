import math
for i in range(3):
    print("welcom to my calculator")
    print("+ : sum")
    print("- : sub")
    print("* : mul")
    print("* : mul")
    print("/ : div")
    print("sqrt")
    print("log")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("! : factorial")
    print("exit")
    print("please enter you'r choice")
    

    op = input()

    if op== "exit":
        print("thank you for using my app")
        print("Good by")
        break
    if op=="+" or op=="-" or op=="/" or op=="*" :
        num1=float(input("enter first number"))
        num2=float(input("enter first number"))
    else :
        num1=float(input("enter first number"))

    if op =="+":
        result= num1+num2

    elif op =="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            result=("cannot divide by zero")
        else  :   
            result=num1/num2

    elif op=="sqrt":
        if num1>0:
            result=math.sqrt(num1)
        else:
            result=("cannot sqrt by negative number")
    elif op=="log":
        result=math.log(num1)
    elif op=="!":
        result=math.factorial(num1)

    if op=="sin" or op=="cos" or op=="cot" or op=="tan":
        num1=num1* math.pi / 180
        
    if op=="sin":
        result=math.sin(num1)

    if op=="cos":
        result=math.cos(num1)

    elif op=="tan":
        result=math.tan(num1)

    elif op=="cot":
        result=math.cot(num1)

    print (result)

    