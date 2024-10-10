import math
number=int(input("please enter number: "))
i=0
fctoril=1
while fctoril<number:
    i=i+1
    fctoril=fctoril*i
    
if fctoril == number:
    print("Yes")
else:
    print("No")