import random

sum=0
user_mistake=0
good_chars=[]
bad_chars=[]
words_bank=["tree","book","blue","train","fish","woman","life","freedom","iran","sky"]

word=random.choice(words_bank)
word=word.lower()

while user_mistake<6:
    for i in range(len(word)):

        if word[i] in good_chars:
            print(word[i],end="")
          
            
                
        else:
            print("- ",end="")

    user_char=input("please write your guess: ")

    if len(user_char)== 1:
        user_char=user_char.lower()

        if user_char in word:
            sum=sum + (word.count(user_char))
            good_chars.append(user_char)
            print("✔")
            if sum== len(word):
                print(word)
                print("✨✨✨you win✨✨✨")
                user_mistake =7

        else:
            bad_chars.append(user_char)
            user_mistake +=1
            print("✖")
    
    else:
        print("please enter a letter")


if user_mistake==6:
    print("game over")

print("FINISH")