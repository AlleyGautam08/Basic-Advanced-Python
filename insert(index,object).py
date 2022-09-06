from plistlib import InvalidFileException


a=[]
for i in range(6):
     x=input("enter value")
     a.append(x)
print("original list is:",a)
index=int(input("enter index where you want to insert:"))
value=input("enter value to insert:")
a.insert(index.value)
print("list after insertion:",a)