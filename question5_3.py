
user=int(input("enter the number"))
x=0
y=1
i=0
while i<=user:
    if i%2==0:
        print(i)
    x=y
    y=i
    i=x+y


   