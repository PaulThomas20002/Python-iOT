i=1
sum=0
while(i<11):
    print("i = ",i)
    i=i+1
##
i=321
print(i)
while i>0:
    d=i%10
    sum=sum*10+d
    i=int(i/10)
print(sum)
##
paul="Paul"
paul1="PAUL"
print(paul,paul1)
#
#
sum=0
a=int(input("Enter the num:"))
b=a
print(a)
while a>0:
    d=a%10
    sum=sum+d*d*d
    a=int(a/10)
print(sum)
if sum==b:
    print("Arstrong yea",b)
else:
    print("Not armstrong")
