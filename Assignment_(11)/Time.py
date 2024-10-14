import datetime

class Time:
    #property
    def __init__(self,h,m,s):
        self.hour=h
        self.minet=m
        self.second=s
        self.chek()

    #metod
    def show(self):
        print(self.hour,":",self.minet,":",self.second)

    def second_to_time(self,t):
        self.hour=int(t/3600)
        self.minet=int((t-(3600*self.hour))/60)
        self.second=t-(3600*self.hour+60*self.minet)
        self.show()

    def time_to_second(self):
        seconds=(self.hour*3600)+(self.minet*60)+self.second
        return seconds
    
    def sum(self,t):
        h=self.hour + t.hour
        m=self.minet + t.minet
        s=self.second + t.second
        result=Time(h,m,s)
        return result 
    
    def sub(self,t):
        a=self.time_to_second()
        b=t.time_to_second()
        if a>b:
            h=self.hour - t.hour
            m=self.minet - t.minet
            s=self.second - t.second
        else:
            h=t.hour - self.hour
            m=t.minet - self.minet
            s=t.second - self.second
        result=Time(h,m,s)
        return result

    def GMT_to_Tehran(self):
        x = datetime.datetime.utcnow()
        hour=int(x.strftime("%I"))+3
        minet=int(x.strftime("%M"))+30
        second=int(x.strftime("%S"))
        result=Time(hour,minet,second)
        return result

    def chek(self):
        if self.minet<0:
            self.minet+=60
            self.hour-=1
        if self.second<0:
            self.second+=60
            self.minet-=1
        if self.second>=60:
            self.minet+=1
            self.second-=59  
        if self.minet>=60:
            self.minet-=59
            self.hour+=1


time_test=Time(0,0,0)
choice=""
while choice!="exit":
    choice=input("Enter your choice:sub, sum, time_to_second, second_to_time, GMT_to_Tehran, exit: ")
    if choice=="sub" or choice=="sum" :
        h=int(input("please enter hour1:"))
        m=int(input("please enter minet1:"))
        s=int(input("please enter second1:"))
        time1=Time(h,m,s)
        h=int(input("please enter hour2:"))
        m=int(input("please enter minet2:"))
        s=int(input("please enter second2:"))
        time2=Time(h,m,s)
        if choice=="sub":
            result=time1.sub(time2)
            result.show()
        if choice=="sum":
            result=time1.sum(time2)
            result.show()
    
    if choice=="time_to_second" :
        h=int(input("please enter hour:"))
        m=int(input("please enter minet:"))
        s=int(input("please enter second:"))
        time=Time(h,m,s)
        result=time.time_to_second()
        print("seconds: ",result)

    if choice=="GMT_to_Tehran":
        result=time_test.GMT_to_Tehran()
        result.show()
            
    if choice=="second_to_time":
        seconds=int(input("enter seconds:"))
        time_test.second_to_time(seconds)


print("Thank you.😎")

