import qrcode

name=input("please enetr your name: ")
phone=input("please enetr your phone: ")

image=qrcode.make(name+phone)
image.save ("my_qrcode.png")