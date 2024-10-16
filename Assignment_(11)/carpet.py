def chek(n):
    if n%5==0:
        return "🥭"
    if n%5==1:
        return "🍐"
    if n%5==2:
        return "🍇"
    if n%5==3:
        return "🍒"
    if n%5==4:
        return "🌽"


def carpet(n):
    if (n%2)!=0:
        m = n // 2
        return [[chek(max(abs(x - m), abs(y - m))) for x in range(n)] for y in range(n)]
    else:
        return "✖"
    
def show(list):
    if len(list)==1:
       print("n not even number.")
    else:
        for row in list:
            print()
            for cell in row:
              print(cell,end="")
          

n=int(input("Enter N: "))
result=carpet(n)
show(result)