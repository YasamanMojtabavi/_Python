n = int(input("enter list length :"))
list_number=[]
newlist_number=[]
for i in range (n) :
    x =int(input("enter number :"))
    list_number.append(x)

for number in list_number:
    if number not in newlist_number:
        newlist_number.append(number)
        
print(newlist_number)  