import pyfiglet
import random
import time
from colorama import Fore , init

init()
title=pyfiglet.figlet_format("Tic Tac Toe",font="slant")
print(title)

print("<<< Menu >>>")
print("Player vs CPU : 1")
print("Player vs Player : 2")
choice=int(input("Enter your choice: "))

start = time.time()

game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

def show():
    for row in game_board:
     for cell in row:
        if cell =="o":
         print( Fore.BLUE +"o",end="")
         print(Fore.WHITE + "",end="")
        elif cell =="x":
            print( Fore.RED + "x",end="")
            print(Fore.WHITE + "",end="")
        else:
            print(cell,end="")
     print()
  


def check_game(z):
    for row in range(3):
        bool=True
        for col in range(3):
            if game_board[row][col]!=z:
                bool=False
        if bool==True:
         print("✨🎉✨",z,"is win.✨🎉✨")
         print(" ⏰⌛Run Time⌛⏰ : " + str( time.time() - start ))
         exit()
    
    for col in range(3):
        bool=True
        for row in range(3):
            if game_board[row][col]!=z:
                bool=False
        if bool==True:
         print("✨🎉✨",z,"is win.✨🎉✨")
         print(" ⏰⌛Run Time⌛⏰ : " + str( time.time() - start ))
         exit()
    
    bool=True
    for row_col in range(3):
        if game_board[row_col][row_col]!=z:
            bool=False
    if bool==True:
        print("✨🎉✨",z,"is win.✨🎉✨")
        print(" ⏰⌛Run Time⌛⏰ : " + str( time.time() - start ))
        exit()
    
    bool=True
    for row_col in range(2,-1,-1):
        if game_board[row_col][2-(row_col)]!=z:
            bool=False
    if bool==True:
         print("✨🎉✨",z,"is win.✨🎉✨")
         print(" ⏰⌛Run Time⌛⏰ : " + str( time.time() - start ))
         exit()

    bool=True
    for row in range(3):
     for col in range(3):
        if game_board[row][col]=="-":
            bool=False
    if bool==True:
         print("😐😐😐 O == X 😐😐😐")
         print(" ⏰⌛Run Time⌛⏰ : " + str( time.time() - start ))
         exit()




if choice==2:   
    show()
    while True:
        print("'Player 1'")
        while True:
            row=int(input("row: "))
            col=int(input("col: "))

            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="-":
                    game_board[row][col]="x"
                    break
                else:
                    print("Try again.")
            else:
             print("The number of rows and columns allowed is 3.")

        show()
        check_game("x")

        print("'Player 2'")
        while True:
            row=int(input("row: "))
            col=int(input("col: "))
            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="-":
                    game_board[row][col]="o"
                    break
                else:
                    print("Try again.")
            else:
                print("The number of rows and columns allowed is 3.")
        
        show()
        check_game("o")

if choice==1:
    show()
    while True:
        print("'Player 1'")
        while True:
            row=int(input("row: "))
            col=int(input("col: "))

            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="-":
                    game_board[row][col]="x"
                    break
                else:
                    print("Try again.")
            else:
             print("The number of rows and columns allowed is 3.")

        show()
        check_game("x")

        print("'Player 2'")
        while True:
            row=random.randint(0,2)
            col=random.randint(0,2)
            if game_board[row][col]=="-":
                game_board[row][col]="o"
                break
            else:
                print("Try again.")
        
        show()
        check_game("o")

