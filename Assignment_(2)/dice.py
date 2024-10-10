import random
x="yes"
while x=="yes":
    x=str(input("Do you want to roll the dice?"))
    dice=random.randint(1,6)
    print(dice)
    if dice==6:
        x=str(input("✨you win✨ & you can roll again,do you want?"))
        if x=="yes":
         print(dice)

   
print("finish")