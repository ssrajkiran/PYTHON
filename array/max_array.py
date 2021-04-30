def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
        return max
x=[int(x) for x in input("Enter value:").split()]
n = len(x)
Ans = largest(x,n)
print ("Largest in given array is",Ans)
