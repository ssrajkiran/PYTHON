list1=input("Enter the list1:").split()
list2=input("Enter the list2:").split()
search=input("Enter the number to search:")
count1=0
count2=0
for i in list1:
    if i==search:
        count1+=1
print("Element present in list1:{}".format(count1))

for j in list2:
    if j==search:
        count2+=1
print("Element present in list2:{}".format(count2))

if count1==count2:
    print("Equal :{}".format(count1))
elif count1<=count2:
    print("Max of number present:{}".format(count2))
elif count1>=count2:
    print("Max of number present:{}".format(count1))
else:
    print("No element found")

