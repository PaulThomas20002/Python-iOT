import calclib as fn
d=1
while d!=5:
 print("Menu\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit\n")
 d=int(input("Enter the Option : "))
 if d!=5:
  x=int(input("Enter the Num1 : "))
  y=int(input("Enter the Num2 : "))
 if d==1:
     fn.add(x,y)
 elif d==2:
     fn.sub(x,y)
 elif d==3:
     fn.mul(x,y)
 elif d==4:
     fn.div(x,y)
