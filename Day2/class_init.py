class Myclass:
    def __init__(self,p,q):
        self.x=p
        self.y=q
    def addtwo(self):
        c=self.x+self.y
        return c
    def subtwo(self):
        c=self.x-self.y
        return c


e=int(input("Enter the Num1: "))
d=int(input("Enter the Num2: "))
c=Myclass(e,d)
z=c.addtwo()
g=c.subtwo()
print("Sum = ",z)
print("Sub=",g)
