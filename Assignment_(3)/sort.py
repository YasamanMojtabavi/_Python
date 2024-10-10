n = int(input("enter list length :"))
list_number=[]
for i in range (n) :
    x =int(input("enter number element :"))
    list_number.append(x)
    
for i in range(len(list_number)):
     for j in range(i+1,len(list_number)):
        if list_number[i]>list_number[j]:
            print("your list not sort.")
            list_number.sort()
            print("sort list : ", list_number)
            exit()
print("your list is sort.")
