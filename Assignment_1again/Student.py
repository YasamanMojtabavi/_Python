
name=input("please enter name:")
family=input("please enter family:")
print("Please enter the grades for the courses:")
cours1=float(input("course1 :"))
cours2=float(input("course2 :"))
cours3=float(input("course3 :"))

average=(cours1+cours2+cours3)/3

if average>=17:
    print(name,family,"educational status:Great")
elif 17>average>=12:
    print(name,family,"educational status:Normal")
elif average<12:
    print(name,family,"educational status:Fail")
