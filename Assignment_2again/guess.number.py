import random

computer_number=random.randint(0,100)
for i in range(20):
    user_number=int(input("guess number?"))

    if computer_number == user_number:
        print("🎉yoou wiiiiiiiiiiiin🎉")
        print("you succeeded after",i+1,"attempts.")
        break

    elif computer_number>user_number:
        print("⬆⬆⬆go up⬆⬆⬆")

    elif computer_number<user_number:
        print("⬇⬇⬇go down⬇⬇⬇")
