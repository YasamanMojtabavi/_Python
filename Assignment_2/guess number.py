import random

computer_number=random.randint(10,40)

for i in range(10):
    user_number=int(input("your guess :"))

    if computer_number==user_number:
        print("✨ ✨ ✨ you win ✨ ✨ ✨")
        i=i+1
        print("✨✨✨ with", i, "guess ✨✨✨")
        break

    elif computer_number > user_number:
        print(" ⬆⬆⬆⬆ go up ⬆⬆⬆⬆ ")

    elif computer_number < user_number:
        print(" ⬇⬇⬇⬇ go down ⬇⬇⬇⬇ ")



