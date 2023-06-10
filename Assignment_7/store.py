import qrcode
PRODUCTS=[]
old_PRODUCTS=[]
basket_buy=[]


def read_from_database():
    f=open("Assignment_7\database.txt","r")

    for line in f:
        result=line.split(",")
    
        my_dict={"code":result[0],"name":result[1],"price":result[2],"count":result[3]}

        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    f=open("Assignment_7\database.txt","w")

    for product in PRODUCTS:
        new=str(product["code"]) + "," + str(product["name"]) + "," + str(product["price"]) + "," + str(product["count"]) + "\n"
        f.write(new)
        


    f.close()

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Qr Code")
    print("8- Exit")

def add():
    code=input("Enter code: ")
    name=input("Enter name: ")
    price=input("Enter price: ")
    count=input("Enter count: ")
    new_product={'code':code,'name':name,'price':price,'count':count}
    PRODUCTS.append(new_product)

def edit():
    code_input=input("Enter your code: ")
    print("1-name")
    print("2-price")
    print("3-count")
    choice=int(input("Select the field you want: "))
    for product in PRODUCTS:
        if product["code"]==code_input and choice==1 :
            product["name"]=input("new name: ")
        elif product["code"]==code_input and choice==2:
            product["price"]=int(input("new price: "))
        elif product["code"]==code_input and choice==3:
            product["count"]=int(input("new count: "))
    print("Information updated successfully.")
    

def remove():
    code_input=input("Enter your code: ")
    for product in PRODUCTS:
        if product["code"]== code_input:
            PRODUCTS.remove(product)
            break
    print("The desired product has been successfully removed.")


def search():
    user_input=input("Enter your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
           print(product["code"],"\t\t",product["name"],"\t\t",product["price"])
           break
    else:
        print("not found.")

def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
     print(product["code"],"\t\t",product["name"],"\t\t",product["price"])

def buy():
    while True:
        code=input("If your purchase is over, enter 0, otherwise, enter the desired code: ")
        if code!= "0":
            for product in PRODUCTS:
                if product["code"]==code:
                    count=int(input("How many of this item do you need?"))
                    Original_count=int(product["count"])

                    if Original_count<count:
                        print("Not enough in stock!")
                    else:
                        Original_count=Original_count-count
                        product["count"]=Original_count
                        new_basket_buy={"code":product["code"],"name":product["name"],"price":product["price"],"count":count}
                        basket_buy.append(new_basket_buy)
                    break
            else: 
                print("not found.")
        else:
            sum=0
            print("nme","\t","count","\t","price")
            for commodity in basket_buy:
                print(commodity["name"],"\t",commodity["count"],"\t",commodity["price"]) 
                sum+=(int(commodity["price"]) * int(commodity["count"]))
            print("sum: ",sum)
            break


def Qr_code():
    code=input("Enter code: ")
    for product in PRODUCTS:
        if product["code"]==code:
            img=qrcode.make("code:" + product["code"] + " name:" + product["name"] + " price:" + product["price"] + " count:" + str(product["count"]))
            img.save ("Qrcode.png")
            break



print("Welcome to Strawberry Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice=int(input("Enter your choice: "))

    if choice ==1:
        add()
    elif choice ==2:
        edit()
    elif choice ==3:
        remove()
    elif choice ==4:
        search()
    elif choice ==5:
        show_list()
    elif choice ==6:
        buy()
    elif choice ==7:
        Qr_code()
    elif choice ==8:
        write_to_database()
        exit(0)
    else:
        print("choice again: ")

