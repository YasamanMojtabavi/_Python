class time:
 
#properties
 def __init__(self,h,m,s):
  self.hours=h
  self.minet=m
  self.second=s

#methods
 def time_to_second(self):
  self.second_time=(self.hours*3600)+(self.minet*60)+self.second
 
 def second_to_time(self):
  ...

def add_time(self):
 ...

def format_12hr(self):
 ...