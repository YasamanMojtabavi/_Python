def khayam(n):
    pascalll=[]
    for i in range(n):
        pascalll.append([1]*(i+1))
        
    for i in range(2,n):
        for j in range(1,i):
            pascalll[i][j] = pascalll[i-1][j-1] + pascalll[i-1][j]
    return pascalll

N=int(input("Enter N:"))
my_kh = khayam(N)
for satr in my_kh:
    print(satr)