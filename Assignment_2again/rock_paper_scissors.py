import random
computer_score=0
user_score=0
cpu_choice=random.randint(1,3)
if cpu_choice==1:
    computer_choice="rock"
elif cpu_choice==2:
    computer_choice="paper"
elif cpu_choice==3:
    computer_choice="scissors"

user_choice=input("enter your choice")

print("💻:",computer_choice)
print("👩🏻‍💻:",user_choice)

if computer_choice =="rock" and user_choice=="paper":
    user_score=user_score+1

elif computer_choice =="rock" and user_choice=="scissors":
    computer_score=computer_score+1

elif computer_choice =="paper" and user_choice=="rock":
    computer_score=computer_score+1

elif computer_choice =="paper" and user_choice=="scissors":
    user_score=user_score+1

elif computer_choice =="scissors" and user_choice=="rock":
    user_score=user_score+1

elif computer_choice =="scissors" and user_choice=="paper":
    computer_score=computer_score+1

if user_score>computer_score:
    print("user is win")
if user_score<computer_score:
    print("computer is win")
else:
    print(" computer=user ")