number=int(input("please enter number: "))
test=1
for i in range (1,number):
    test=test*i
    if test ==number:
        print("yes")
        break
    elif i== number-1:
        print("No")