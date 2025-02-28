import pyfiglet
import datetime
import random
from colorama import Fore, init

init()
title=pyfiglet.figlet_format("Tic Tac Toe",font="slant")
print(title)

game_board=[["_","_","_"],
            ["_","_","_"],
            ["_","_","_"],]

def Menu():
   print("Player vs Player Enter: 1")
   print("Player vs Player Enter: 2")
   choice=int(input("your choice: "))
   return choice

def show():
    for i in range(3):
        for j in range(3):
            if game_board[i][j]=="x":
             print(Fore.RED + "x",end="")
             print(Fore.WHITE + "",end="")
            elif game_board[i][j]=="o":
             print(Fore.BLUE + "o",end="")
             print(Fore.WHITE + "",end="")
            else:
               print(Fore.WHITE + "",end="")
               print(game_board[i][j],end="")
        print()

def chek_print(chek,choice):
    if chek==1:
        print("✨✨✨player1 is win.✨✨✨")
    elif chek==2 and choice==1:
        print("✨✨✨player2 is win.✨✨✨")
    elif chek==2 and choice==2:
        print("✨✨✨CPU is win.✨✨✨")
    elif chek==0:
        print("player1=player2")

def chek_win(lst):
    if lst==["x","x","x"]:
             return 1
    if lst==["o","o","o"]:
             return 2 
    else:  
       return 3
         
def chek_game():
 switch=3
 for i in range(3):
    win_satr=[]
    for j in range(3):
        win_satr.append(game_board[i][j])
    switch=chek_win(win_satr)
    if switch!=3:
     return switch

 for i in range(3):
    win_satr=[]
    for j in range(3):
        win_satr.append(game_board[j][i])
    switch=chek_win(win_satr)
    if switch!=3:
     return switch

 win_satr=[]
 for i in range(3):
     win_satr.append(game_board[i][i])
     if i==2:
      switch=chek_win(win_satr)
      if switch!=3:
       return switch

 win_satr=[]
 j=2
 for i in range(3):
    win_satr.append(game_board[i][j])
    j-=1
    if i==2:
      switch=chek_win(win_satr)
      if switch!=3:
       return switch
 sum=0
 for i in range(3):
    for j in range(3):
        if game_board[i][j]=="_":
            sum=1
 if sum==1:
    return switch
 else:
    return 0 

choice=Menu()
a=datetime.datetime.now()
if choice==1:
    show()
    chek=3
    while chek==3:
        print("Player 1")
        while chek==3:
            row=int(input("row: "))
            col=int(input("col: "))
            if 0<= row <=2 and 0 <= col <= 2:
                if game_board[row][col]=="_":
                    game_board[row][col]="x"
                    break
                else:
                    print("enter new row & col: ")
            else:
                print("Try again")
        show()
        chek=chek_game()
        chek_print(chek,choice)
        if chek!=1:
         print("Player 2")
        while chek==3:
            row=int(input("row: "))
            col=int(input("col: "))
            if 0<= row <=2 and 0 <= col <= 2:
                if game_board[row][col]=="_":
                    game_board[row][col]="o"
                    break
                else:
                    print("enter new row & col: ")
            else:
                print("Try again")
        
        chek=chek_game()
        if chek!=1:
         chek_print(chek,choice)
         show()

elif choice==2:
   show()
   chek=3
   while chek==3:
        print("Player 1")
        while chek==3:
            row=int(input("row: "))
            col=int(input("col: "))
            if 0<= row <=2 and 0 <= col <= 2:
                if game_board[row][col]=="_":
                    game_board[row][col]="x"
                    break
                else:
                    print("enter new row & col: ")
            else:
                print("Try again")
        show()
        chek=chek_game()
        chek_print(chek,choice)
        if chek!=1:
         print("CPU")
        while chek==3:
            row=random.randint(0,2)
            col=random.randint(0,2)
            if 0<= row <=2 and 0 <= col <= 2:
                if game_board[row][col]=="_":
                    game_board[row][col]="o"
                    break

                else:
                    print("enter new row & col: ")
            else:
                print("Try again")
        chek=chek_game()
        if chek!=1:
         show()
         chek_print(chek,choice)


b=datetime.datetime.now()
c=b-a
print("Time of play :",int(c.total_seconds()),"second")











        