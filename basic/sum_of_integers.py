a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
sum=0
if a==b:
    print("Same number you choose! Give range")
else:    
    while a<=b:
        sum+=a
        a=a+1
print(sum)    
