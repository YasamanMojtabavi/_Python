import random
user_mistakes=0

words_bank=["tree","book","green","king","fish","woman","life","train","car"]
true_char=[]
false_char=[]

word=random.choice(words_bank)

while user_mistakes<len(word):
    for i in range(len(word)):
        false=0
        if word[i] in true_char:
            print(word[i],end="")
        elif word[i] in false_char:   
            print("✖",end="")
            false=1
        else:
            print(" _ ",end="")
            false=1
    if false ==1:
        guess_char=input("please enter your guess: ")
        if len(guess_char)==1:
            if guess_char.lower() in word:
                true_char.append(guess_char.lower())
                print("✔")
            else:
                false_char.append(guess_char.lower())
                user_mistakes +=1
                print("✖")
        else:
            print("you can guess one char!!!")
    else:
        print("  yoooou wiiiiiiiin.")
        break

if user_mistakes == len(word):
    print("Game Over")