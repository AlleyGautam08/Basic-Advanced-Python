a=[]
size=int(input("enter size of the list:"))
for i in range(size):
     val=int(input("enter number:"))
     a.append(val)
key=int(input("enter number to search:"))
flag=0
for i in range(size):
     if(a[i]==key):
          flag=1
          pos=i+1
          break
     if(flag==1):
          print("element found at:","pos","position:")
else:
      print("element not found:")
