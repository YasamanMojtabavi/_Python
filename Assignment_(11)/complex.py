class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image


#metods
    def sum(self,c):
        r=self.real+c.real
        i=self.image+c.image
        result=Complex(r,i)
        return result
    
    def sub(self,c):
        r=self.real-c.real
        i=self.image-c.image
        result=Complex(r,i)
        return result
    
    def multi(self,c):
        r=(self.real*c.real)+(-1*(self.image*c.image))
        i=(self.image*c.real)+(self.real*c.image)
        result=Complex(r,i)
        return result
    
    def show(self):
        print(self.real,"+ i",self.image)
    

choice=""
while choice!="exit":
    choice=input("Enter your choice:sub, sum, multi, exit: ")
    if choice=="sub" or choice=="sum" or choice=="multi":
        r=int(input("please enter real1:"))
        i=int(input("please enter image1:"))
        c1=Complex(r,i)
        r=int(input("please enter real2:"))
        i=int(input("please enter image2:"))
        c2=Complex(r,i)
        if choice=="sub":
            result=c1.sub(c2)
            result.show()
        if choice=="sum":
            result=c1.sum(c2)
            result.show()
        if choice=="multi":
            result=c1.multi(c2)
            result.show()



print("Thank you.😎")

a=Complex(5,8)
a.show()