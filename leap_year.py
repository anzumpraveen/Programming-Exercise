user=int(input("enter the year"))
i=0
while i<=user:
    if user%400==0 and user%100!=0 or user%4==0 :
        print(user,"leap year")
        break
    else:
        print("not leap year")
        break
    i+=1


    
    