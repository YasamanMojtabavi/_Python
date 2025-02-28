
scond=int(input("please enter second : "))

hours=scond//3600
scond=scond - (hours*3600)

minute=scond//60
scond=scond - (minute*3600)

 
print(hours,":",minute,":",scond)