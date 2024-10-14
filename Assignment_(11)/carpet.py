def carpet(n):
    if (n%2)!=0:
        m = n // 2
        return [[max("🤑💲") for x in range(n)] for y in range(n)]
    else:
        return "✖"
    
def show(list):
    if len(list)==1:
       print("n not even number.")
    else:
        for row in list:
          print(row)

n=int(input("Enter N: "))
result=carpet(n)
show(result)