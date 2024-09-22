import gtts
words_bank=[]

def read_from_file():
    f=open("D:\python\Python\Assignment_8again/translate.txt","r")

    temp=f.read().split("\n")
    
    for i in range(0,len(temp),2):
        word={"en":temp[i],"fa":temp[i+1]}
        words_bank.append(word)

    f.close()

def write_to_database():
    f=open("D:\python\Python\Assignment_8again/translate.txt","w")
    
    bool=0
    for word in words_bank:
       if bool==0:
            new=str(word["en"]) + "\n" + str(word["fa"])  
            f.write(new)
            bool=1
       else:  
            new=str("\n"+word["en"]) + "\n" + str(word["fa"])  
            f.write(new)
            
    f.close()

def add():
    english=input("Enter english: ")
    fa=input("Enter persian: ")
    new_word={'en':english,'fa':fa}
    words_bank.append(new_word)

def translate_english_to_persian():
    user_text=input("Enter your english text: ")
    user_words=user_text.split(" ")
    output=""

    for user_word in user_words:
        for word in words_bank:
            if word["en"]==user_word:
                output=output + word['fa']+" "
                break
            elif user_word == ".":
                output=output +"."+" "
                break
        else:
            output=output+ user_word +" "

    voice=gtts.gTTS(output,lang="ar",slow=False)
    voice.save("D:\python\Python\Assignment_8again/voice.mp3")
    print(output)

def translate_persian_to_english():
    user_text=input("Enter your persian text: ")
    user_words=user_text.split(" ")
    output=""

    for user_word in user_words:
        for word in words_bank:
            if word["fa"]==user_word:
                output=output + word['en']+" "
                break
            elif user_word == ".":
                output=output +"."+" "
                break

        else:
            output=output+ user_word +" "

    voice=gtts.gTTS(output,lang="en",slow=False)
    voice.save("D:\python\Python\Assignment_8again/voice.mp3")
    print(output)

def show_menu():
    print("welcom to my translate")
    print("1-Translate english to persian.")
    print("2-Translate persian to english.")
    print("3-Add a new word to database.")
    print("4-Exit.")

read_from_file()

while True:
    show_menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        translate_english_to_persian()
    elif choice==2:
        translate_persian_to_english()
    elif choice==3:
        add()
    elif choice==4:
        write_to_database()
        exit(0)


    