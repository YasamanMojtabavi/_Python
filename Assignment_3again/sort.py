arrey=[]
n=int(input("Please enter lenght list: "))
for i in range(n):
    arrey.append(int(input("number: ")))

b=1

for i in range(1,n):
    if arrey[i]<arrey[i-1]:
        b=0
        
if b==1:
 print("sort is true.")
else:
   print("sort is false.")