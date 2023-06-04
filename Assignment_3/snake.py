import random
N=int(input("please enter number: "))
snake_N=[]

while len(snake_N) != N:
    if ((len(snake_N)) % 2 ) == 0 :
        snake_N.append("*")
        print("*",end="")
    else:
         snake_N.append("#")
         print("#",end="")

    


