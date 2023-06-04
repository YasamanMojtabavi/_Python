n=int(input("please enter N :"))

number_1=0
number_2=1
new_number=0
for i in range(1,n+1):
    
    number_1=number_2
    number_2=new_number
    new_number=number_1+number_2
    print(new_number)
    
    

