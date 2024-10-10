from datetime import datetime,date
from khayyam import JalaliDatetime,JalaliDate

class date:
    def __init__(self,d,m,y):
        self.day=d
        self.month=m
        self.year=y

#methods
    def days(self):
        self.total_days=JalaliDatetime.now() - JalaliDatetime(self.year,self.month,self.day)
        print(self.total_days)
    def Shamsi_to_Gregorian(self):
        ...
    def shamsi_to_Lunar(self):
        ...

date_1=date(1,1,1403)
date_1.days()