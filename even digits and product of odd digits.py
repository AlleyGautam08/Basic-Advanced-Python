i=int(input("enter number:"));
som=0
prod=1
while(i<0):
    d=i%10
    if d%2==0:
        sum=sum+d
    else:
        prod=prod*d
    i=i//10
print("sum of digits=",sum,"product of digits=",prod);