class Myclass:
    def addtwo(self,a,b):
        return a+b
c=Myclass()
x=int(input("Enter the Num1: "))
y=int(input("Enter the Num2: "))
z=c.addtwo(x,y)
print("Sum = ",z)
