def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
d=1
while d!=5:
 print("Menu\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit\n")
 d=int(input("Enter the Option : "))
 if d<5:
  x=int(input("Enter the Num1 : "))
  y=int(input("Enter the Num2 : "))
 if d==1:
     add(x,y)
 elif d==2:
     sub(x,y)
 elif d==3:
     mul(x,y)
 elif d==4:
     div(x,y)
 else:
     print("Invalid Input")
