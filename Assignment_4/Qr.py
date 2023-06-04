import qrcode

username=input("please enter your name: ")
user_phon_number=input("please enter your phone: ")

img=qrcode.make(username+user_phon_number)
img.save ("Qrcode.png")