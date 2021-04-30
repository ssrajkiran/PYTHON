a=input("Enter the list:")
list=a.split()
print(list)
for i in range(len(list)):
    list[i]=int(list[i])
print("sum =",sum(list))    
