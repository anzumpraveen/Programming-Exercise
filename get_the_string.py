st="srishti"
x=(st[0])
y=(st[1])
z=(st[-2])
m=(st[-1])
print(x+y+z+m)
# secon method
a="srtyuing"
i=0
b=""
while i<len(a):
    if i==0:
        b=b+a[i]
    if i==1:
        b=b+a[i]
        b=b+a[-i-1]
        b=b+a[-i]
    i+=1
print(b)

    
