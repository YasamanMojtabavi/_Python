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
         soorat=self.soorat*s
         makhraj=self.makhraj*m
         print(soorat ,"/" , makhraj)

    def sum(self,s,m):
        if self.makhraj==m:
            soorat=self.soorat+s
            makhraj=m
        else:
            soorat=(self.soorat*m)+(s*self.makhraj)
            makhraj=self.makhraj*m
        print(soorat ,"/" , makhraj)

    def divis(self,s,m):
        soorat=self.soorat*m
        makhraj=self.makhraj*s
        print(soorat ,"/" , makhraj)

    def sub(self,s,m):
        if self.makhraj==m:
            soorat=self.soorat-s
            makhraj=m
        else:
            soorat=(self.soorat*m)-(s*self.makhraj)
            makhraj=self.makhraj*m
        print(soorat ,"/" , makhraj)


s_1=int(input("please enter numerator of fraction1:"))
m_1=int(input("please enter denominator of fraction1:"))
s_2=int(input("please enter numerator of fraction2:"))
m_2=int(input("please enter denominator of fraction2:"))
my_kasr1=kasr(s_1,m_1)
my_kasr2=kasr(s_2,m_2)
choice=input("Enter your choice:sub, divis, sum, multi: ")
if choice=="sub":
    my_kasr1.sub(my_kasr2.soorat,my_kasr2.makhraj)
if choice=="divis":
    my_kasr1.divis(my_kasr2.soorat,my_kasr2.makhraj)
if choice=="sum":
    my_kasr1.sum(my_kasr2.soorat,my_kasr2.makhraj)
if choice=="multi":
    my_kasr1.multi(my_kasr2.soorat,my_kasr2.makhraj)

