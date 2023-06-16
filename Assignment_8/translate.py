import gtts

def menu():
    print("1- English ➡  Persion")
    print("2- Persion ➡  English")
    print("3- Add word")
    print("4- exit")
    choice=input("Enter your choice: ")
    return choice

def read_from_file():
    global words_bank
    f=open("Assignment_8/translate.txt","r")
    temp=f.read().split("\n")
    words_bank=[]
    for i in range(0,len(temp),2):
         my_dict={"en":temp[i],"fa":temp[i+1]}
         words_bank.append(my_dict)
    f.close()

def write_to_file():
    f=open("Assignment_8/translate.txt","w")
    for dict in words_bank:
        new=str(dict["en"]) + "\n" + str(dict["fa"]) +"\n"
        f.write(new)
        
    f.close()

def english_to_persian():
    user_text=input("Enter your english text:")
    user_words=user_text.split(" ")
    out_put=''
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                out_put=out_put+(word["fa"])+" "
                break
        else:
            out_put=out_put+(user_word)+" "
    print(out_put)

def persian_to_english():
    user_text=str(input("Enter your persian text:")).replace("."," ")
    user_words=user_text.split(" ") 
    out_put=''
    for user_word in user_words:
        for word in words_bank:
            if user_word ==".":
                out_put=out_put + "."
            elif user_word == word["fa"]:
                out_put=out_put+(word["en"])+" "
                break
        else:
            out_put=out_put+(user_word)+" "
    teext=out_put
    voice=gtts.gTTS(teext,lang="en",slow=False)
    voice.save("Assignment_8/voice.mp3")
    print(out_put)

def add_word():
     temp_en=input("write your english word: ")
     temp_fa=input("mean: ")
     my_dict={"en":temp_en,"fa":temp_fa}
     words_bank.append(my_dict)
     write_to_file()

read_from_file()
while True:
    choice=int(menu())
    if choice==1:
        english_to_persian()
    elif choice==2:
        persian_to_english()
    elif choice==3:
        add_word()
    elif choice==4:
        exit()

