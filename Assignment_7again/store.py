import qrcode
PRODUCTS=[]

def read_from_database():
    f=open("D:\python\Python\Assignment_7again\database.txt","r")

    for line in f:
        result=line.split(",")
        count=result[3]
        my_dict={'code':result[0],'name':result[1],'price':result[2],'count':count.replace("\n","")}
        PRODUCTS.append(my_dict)
    f.close()

def write_to_database():
    f=open("D:\python\Python\Assignment_7again\database.txt","w")

    for product in PRODUCTS:
        new=str(product["code"]) + "," + str(product["name"]) + "," + str(product["price"]) + "," + str(product["count"]) + "\n"
        f.write(new)
        
    f.close()

def add():
    code=input("Enter code: ")
    name=input("Enter name: ")
    price=input("Enter price: ")
    count=input("Enter count: ")
    new_dict={'code':code,'name':name,'price':price,'count':count}
    PRODUCTS.append(new_dict)

def edit():
    user_code=input("Enter code: ")
    print("1-Name")
    print("2-price")
    print("3-count")
    choic=int(input("Which of the above do you want to edit? "))
    
    for product in PRODUCTS:
        if product['code']==user_code:
            if choic==1:
                product['name']=input("Enter name: ")
            if choic==2:
                product['price']=input("Enter price: ")
            if choic==3:
                product['count']=input("Enter count: ")
            print("Information updated successfully.")
            break
    else:
        print("not found.")

def remove():
    user_code=input("Enter code: ")
    for product in PRODUCTS:
        if product['code']==user_code:
            PRODUCTS.remove(product)
    print("The desired product has been successfully removed.")

def search():
    user_input=input("Type your keyword: ")
    for product in PRODUCTS:
        if product['code']==user_input or product['name']==user_input:
            print(product['code'],"\t\t",product['name'],"\t\t",product['price'])
            break
    else:
        print("not found.")

def show_list():
    print("Code\t\tName\t\tPrice")
    for product in PRODUCTS:
         print(product['code'],"\t\t",product['name'],"\t\t",product['price'])

def buy():
    bill=[]
    total_sum=0
    while True:
        chooice=input("Buy or exit?")
        if chooice =="buy":
            user_code=input("Enter code: ")
            for product in PRODUCTS:
                if product['code']==user_code:
                    count=int(input("Please enter the desired number of the selected product?"))
                    if int(product['count'])<count:
                        print("Insufficient inventory.")
                    else:
                        product['count']=int(product['count'])-count
                        shop={'name':product['name'],'price':product['price'],'count':count}
                        bill.append(shop)

                    break
            else:
                print("not found.")
        else:
            print("Count\t\tName\t\tPrice")
            for product in bill:
                 print(product['count'],"\t\t",product['name'],"\t\t",product['price'])
                 count=int(product["count"])
                 price=int(product["price"])
                 total_sum=total_sum+(count*price)
            print("sum: ",total_sum)
            break

def Qr_code():
    user_code=input("Enter code: ")
    for product in PRODUCTS:
        if product['code']==user_code:
            code=product['code']
            name=product['name']
            price=product['price']
            count=product['count']
            img=qrcode.make(code+name+price+count)
            img.save ("Qrcode.png")

def show_menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-show List")
    print("6-Buy")
    print("7-Qr code")
    print("8-Exit")

print("😊Wellcome😊")
print("Loading...")
read_from_database()
print("Data Loaded")

while True:
    show_menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice==7:
        Qr_code()
    elif choice==8:
        write_to_database()
        exit(0)
    else:
        print("Your selection is not on the menu.")