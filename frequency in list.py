a=[]
size=int(input("enter size of the list:"))
for i in range(size):
     val=int(input("enter number:"))
     a.append(val)
key=int(input("enter number to find frequency:"))
count=0
for i in range(size):
     if(a[i]==key):
          count=count+1
print("frequency=",count)