Time=int(input("please enter seconds: "))

hours=int(Time/3600)
minet=int((Time-(hours*3600))/60)
second=int((Time-(hours*3600))-(minet*60))

print(hours,":",minet,":",second)