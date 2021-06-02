user=int(input("enter the num="))
user1=int(input("enter the number="))

for num in range(user,user1+1):
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum+=i
        i+=1
    if num==sum:
        print(num,"perfect")
    