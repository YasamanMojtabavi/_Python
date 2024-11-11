import Media
Media=[]
def read_from_database():
    f=open("D:\python\Python\Assignment_(12)\database.txt","r")
    for line in f:
        result=line.split(",")
        my_dict={"type":result[0],"name":result[1],"director":result[2],"IMDB":result[3],"url":result[4],"duration":result[5],"cast":result[6]}
        print(my_dict)
        print(my_dict["type"])

    
        Media.append(my_dict)
    f.close()

read_from_database()

for media in Media:
    print("ff")


def write_to_database():
    f=open("D:\python\Python\Assignment_(12)\database.txt","w")
    for product in Media:
        new=str(product["code"]) + "," + str(product["name"]) + "," + str(product["price"]) + "," + str(product["count"]) + "\n"
        f.write(new)   
    f.close()

