import classmod as fn
#from filename import classname #also crrt
e=int(input("Enter the Num1: "))
d=int(input("Enter the Num2: "))
c=fn.Myclass(e,d) #p & q is assigned with e & d
z=c.addtwo()
g=c.subtwo()
print("Sum = ",z)
print("Sub=",g)
