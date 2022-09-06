a=int(input("enter fisrt number:"));
b=int(input("enter second number:"));
c=int(input("enter third number:"));
if a>b and a>c:
    print("max number=",a);
elif b>a and b>c:
    print("max number=",b);
else:
    print("max number=",c);