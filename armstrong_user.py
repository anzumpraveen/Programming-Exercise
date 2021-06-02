user=int(input("enter the number"))
user2=int(input("enter the 2number"))


for num in range(user,user2 + 1):
    sum=0
    i=num
    while i>0:
        digit=i%10
        sum+=digit**3
        i//=10
    if num==sum:
        print(num,"armstrong")
    