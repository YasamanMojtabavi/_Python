import random
import gtts
import qrcode
import telebot
from telebot import types

my_keyboard=types.ReplyKeyboardMarkup(row_width=2)
key1=types.KeyboardButton("start")
key2=types.KeyboardButton("game")
key3=types.KeyboardButton("age")
key4=types.KeyboardButton("voice")
key5=types.KeyboardButton("max")
key6=types.KeyboardButton("argmax")
key7=types.KeyboardButton("qrcode")
key8=types.KeyboardButton("Help🙃")
my_keyboard.add(key1,key2,key3,key4,key5,key6,key7,key8)

bot = telebot.TeleBot("6149538569:AAHGCejY-o05UPRWkeCAJ5JJlQX2AD9fAQo",parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Hello, please enter your name.")
    bot.send_message(message.chat.id,  "wellcom" + message.txt)
	
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "How can i help?")

@bot.message_handler(commands=["qrcode"])
def send_qrcode(message):
	img=qrcode.make(str(message.txt))
	img.save ("Qrcode.png")
	photo = open('Assignment_9\Qrcode.png', 'rb')
	bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=["age"])
@bot.message_handler(commands=["game"])
@bot.message_handler(commands=["max"])
@bot.message_handler(commands=["argmax"])
@bot.message_handler(commands=["voice"])


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "hello":
		bot.send_message(message.chat.id,"Hello")
		
	else:
		bot.send_message(message.chat.id,"icant understand",reply_markup=my_keyboard)

    
bot.infinity_polling()