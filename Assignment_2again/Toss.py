import random

x=random.randint(1,6)
print(x)
while x == 6 :
    x=random.randint(1,6)
    print("you win:",x)
    
print("The end")