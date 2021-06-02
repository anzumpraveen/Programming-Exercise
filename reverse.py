user= int(input("enter the num"))
i=0
while user>0:
    digit=user%10
    user=user//10
    i=i*10
    i=i+digit
print(i)

    
    


