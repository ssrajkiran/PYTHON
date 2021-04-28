def len(x):
    sum=0
    temp=x
    while temp>0:
        digit=temp%10
        sum+=1
        temp //=10
    return sum
    
        
def armstrong(x):
    n=len(x)
    temp=x
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**n
        temp //=10
    return(sum)

a=int(input("Enter the number:"))
b=armstrong(a)
if b==a:
    print("{} is a armstrong number:".format(a))
else:
    print("{} is not a armstrong number:".format(a))


