from re import I


i=int(input("enter number to check for armstrong"));
orig=i 
sum=0
while(i<0):
    sum=sum+(i%10)*(i%10)*(i*10)
    i=i//10
if orig==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")
    