import qrcode
import random
import gtts
from datetime import datetime,date
from khayyam import JalaliDatetime,JalaliDate
import telebot
from telebot import types

bot = telebot.TeleBot("7763262955:AAGAxDXvPzWpky4fcE0uD4PwjYfedLonqRs", parse_mode=None)

my_keyboard=types.ReplyKeyboardMarkup(row_width=4)
key1=types.KeyboardButton("start")
key2=types.KeyboardButton("🎳game🎳")
key3=types.KeyboardButton("😊age😊")
key4=types.KeyboardButton("🔊voice🔊")
key5=types.KeyboardButton("⬆ max ⬆")
key6=types.KeyboardButton("argmax")
key7=types.KeyboardButton("qrcode")
key8=types.KeyboardButton("🆘 help 🆘")
my_keyboard.add(key1,key2,key3,key4,key5,key6,key7,key8)

@bot.message_handler(commands=['start'])
def send_welcom(message):
	bot.reply_to(message, f"Hello {message.from_user.first_name} , Welcome to my Bot!")




@bot.message_handler(commands=['help'])
def send_menu(message):
	bot.send_message(message.chat.id,"start: welcome." + "\n" + "game: Number guessing game." +"\n" + "age: age calculation by receiving the date of birth." + "\n"+"voice: Convert text to voice. (Enter your sentence in English.)"+"\n"+"max: the largest value of the presentation." +"\n"+"argmax: the index of the largest value of the presentation."+"\n"+"qrcode: make qrcode.", reply_markup=my_keyboard)

  


@bot.message_handler(commands=['voice'])
def send_voice(message) :
    bot.send_message(message.chat.id , "Please enter the sentence that you want to convert to voice .")
    bot.register_next_step_handler(message, voice)

def voice(message) :
    tts = gtts.gTTS(text=message.text, lang='en')
    tts.save("D:\python\Python\Assignment_9again/voice.mp3")
    voice = open("D:\python\Python\Assignment_9again/voice.mp3", "rb")
    bot.send_voice(message.chat.id, voice)




@bot.message_handler(commands=['qrcode'])
def send_photo(message) :
    bot.send_message(message.chat.id , "Please enter the sentence .")
    bot.register_next_step_handler(message, qr)

def qr(message) :
    img=qrcode.make(message.text)
    img.save("Assignment_9again/qrcode.png")
    photo= open("Assignment_9again/qrcode.png", "rb")
    bot.send_voice(message.chat.id, photo)


@bot.message_handler(commands=['age'])
def send_age(message) :
    bot.send_message(message.chat.id , "Enter your date of birth in order of year, month and day.")
    bot.register_next_step_handler(message,age)

def age(message) :
    list=str(message.text).split(" ")
    age=JalaliDatetime.now() - JalaliDatetime(list[0],list[1],list[2])
    bot.send_message(message.chat.id, age)
	
	
	
@bot.message_handler(commands=['max'])
def max_message(message):
    bot.send_message(message.chat.id, "Please enter a list of numbers separated by commas (1,11,22,33,2).")
    bot.register_next_step_handler(message, send_max)

def send_max(message):
    num_list = message.text.split(",")
    num_list = [int(num) for num in num_list]
    max_number = max(num_list)
    bot.reply_to(message, f"The maximum value is {max_number} ." )



@bot.message_handler(commands=['fal'])
def send_fal(message):
	fal_list=["jjj",'lll','mmm']
	selected_fal=random.choice(fal_list)
	bot.send_message(message.chat.id,selected_fal)



@bot.message_handler(func=lambda m:True)
def echo_all(message):
	if message.text=="hello":
		bot.send_message(message.chat.id,"Hello dear.")
		
	elif message.text=="🆘 help 🆘":
		send_menu(message)
					
	elif message.text=="start":
		send_welcom(message)
		
	elif message.text=="🎳game🎳":
		bot.send_message(message.chat.id,"این یک پیام ساده است.")

	elif message.text=="😊age😊":
		send_age(message)

	elif message.text=="qrcode":
		send_photo(message)
		
	elif message.text=="🔊voice🔊":
		send_voice(message)
		
	elif message.text=="⬆ max ⬆":
		send_max(message)
		
	else:
         bot.send_message(message.chat.id,"I cannot understand!")
		
		

bot.infinity_polling()