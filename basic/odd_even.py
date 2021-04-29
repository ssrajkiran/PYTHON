def check(a,b):
    even=0
    odd=0
    for i in range(a,b+1):
        if i%2==0:
            even+=1            
            
        else:
            odd+=1        
    print("Total number :{} is even".format(even))
    print("Total number :{} is odd".format(odd))

a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))
check(a,b)
