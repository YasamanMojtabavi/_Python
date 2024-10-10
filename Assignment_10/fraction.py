class kasr:
#property
    def __init__(self,s,m):
        self.soorat=int(s)
        self.makhraj=int(m)
        kasr.chek(self)
#metod
    def chek(self):
     if self.makhraj==0:
        self.makhraj=int(input("The denominator cannot be zero. Enter a Digit number:"))
     
    def multi(self,s,m):
         self.soorat=self.soorat*s
         self.makhraj=self.makhraj*m

    def sum(self,s,m):
        if self.makhraj==m:
            self.soorat+=s
        else:
            self.soorat=(self.soorat*m)+(s*self.makhraj)
            self.makhraj*=m

    def divis(self,s,m):
        self.soorat=self.soorat*m
        self.makhraj=self.makhraj*s

    def sub(self,s,m):
        if self.makhraj==m:
            self.soorat-=s
        else:
            self.soorat=(self.soorat*m)-(s*self.makhraj)
            self.makhraj*=m
        

my_kasr1=kasr(3,6)
my_kasr2=kasr(2,6)
#my_kasr1.sub(my_kasr2.soorat,my_kasr2.makhraj)
#my_kasr1.divis(my_kasr2.soorat,my_kasr2.makhraj)
#my_kasr1.sum(my_kasr2.soorat,my_kasr2.makhraj)
my_kasr1.multi(my_kasr2.soorat,my_kasr2.makhraj)
print(my_kasr1.soorat , "/" , my_kasr1.makhraj)
