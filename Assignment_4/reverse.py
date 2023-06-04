n = int(input("enter list length :"))
list_number=[]
for i in range (n) :
    x =int(input("enter number :"))
    list_number.append(x)

list_number.reverse()
print(list_number)