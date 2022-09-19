i=1
y=1
z=1
b=[]
sum=0
while i<=10:
    print(z,end=" ")
    if z%2==0:
        sum=sum+z
    i=i+1
    x=y
    y=z
    z=x+y
print("..............sum of even no.",sum)   