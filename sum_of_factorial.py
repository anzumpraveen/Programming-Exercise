
# WRONG

num =(input("enter a number: "))
fac = 1
sum=0
i = 0
while i <len(num):
    no=int(num[i])
    j=1
    fac=1
    while j<=(no):
        fac =fac * j
        j+=1
    sum+=fac
    i = i + 1
print("factorial of ", num, " is ", sum)