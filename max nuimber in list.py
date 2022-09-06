a=[]
size=int(input("enter size of the list:"))
for i in range(size):
     val=int(input("enter number:"))
     a.append(val)
max=a[0]
for i in range(size):
     if(a[i]>max):
          max=a[i]
print("max number=",max)
