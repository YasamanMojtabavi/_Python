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
         new_kasr=kasr(soorat,makhraj)
         return new_kasr

    def sum(self,s,m):
        if self.makhraj==m:
            soorat=self.soorat+s
            makhraj=m
        else:
            soorat=(self.soorat*m)+(s*self.makhraj)
            makhraj=self.makhraj*m
        new_kasr=kasr(soorat,makhraj)
        return new_kasr

    def divis(self,s,m):
        soorat=self.soorat*m
        makhraj=self.makhraj*s
        new_kasr=kasr(soorat,makhraj)
        return new_kasr

    def sub(self,s,m):
        if self.makhraj==m:
            soorat=self.soorat-s
            makhraj=m
        else:
            soorat=(self.soorat*m)-(s*self.makhraj)
            makhraj=self.makhraj*m
        new_kasr=kasr(soorat,makhraj)
        return new_kasr

    def kasr_to_number(self):
        self.number=self.soorat/self.makhraj
        print(self.number)

    def simple(self):
        if abs(self.soorat)>abs(self.makhraj):
            for i in range(abs(self.makhraj),1,-1):
                if self.soorat%i==0 and self.makhraj%i==0:
                    self.soorat/=i
                    self.makhraj/=i
                    break

        elif abs(self.soorat)<abs(self.makhraj):
            for i in range(abs(self.soorat),1,-1):
                if self.soorat%i==0 and self.makhraj%i==0:
                    self.soorat/=i
                    self.makhraj/=i
                    break
        else:
            self.soorat=1
            self.makhraj=1

    def show(self):
        print(self.soorat ,"/" ,self.makhraj)

choice=""
while choice!="exit":
    choice=input("Enter your choice:sub, divis, sum, multi, number, simple, exit: ")
    if choice=="sub" or choice=="divis"or choice=="sum" or choice=="multi":
        s_1=int(input("please enter numerator of fraction1:"))
        m_1=int(input("please enter denominator of fraction1:"))
        my_kasr1=kasr(s_1,m_1)
        s_2=int(input("please enter numerator of fraction2:"))
        m_2=int(input("please enter denominator of fraction2:"))
        my_kasr2=kasr(s_2,m_2)
        if choice=="sub":
            result=my_kasr1.sub(my_kasr2.soorat,my_kasr2.makhraj)
            result.show()
        if choice=="divis":
            result=my_kasr1.divis(my_kasr2.soorat,my_kasr2.makhraj)
            result.show()
        if choice=="sum":
            result=my_kasr1.sum(my_kasr2.soorat,my_kasr2.makhraj)
            result.show()
        if choice=="multi":
            result=my_kasr1.multi(my_kasr2.soorat,my_kasr2.makhraj)
            result.show()
            
    elif choice=="number":
        s_1=int(input("please enter numerator of fraction:"))
        m_1=int(input("please enter denominator of fraction:"))
        my_kasr1=kasr(s_1,m_1)
        my_kasr1.kasr_to_number()
    elif choice=="simple":
        s_1=int(input("please enter numerator of fraction:"))
        m_1=int(input("please enter denominator of fraction:"))
        my_kasr1=kasr(s_1,m_1)
        my_kasr1.simple()
        print(int(my_kasr1.soorat) ,"/", int(my_kasr1.makhraj))

print("Thank you.😎")