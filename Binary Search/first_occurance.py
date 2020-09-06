arr=[2,4,10,10,10,10,18,20]
element=10
i=0
j=len(arr)-1
res=-1

while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        res=mid
        j=mid-1
    else:
        if(arr[mid]>element):
            j=mid-1
        else:
            i=mid+1
    
print("First Occurance Position: {}".format(res))

i=0
j=len(arr)-1
while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        res=mid
        i=mid+1
    else:
        if(arr[mid]>element):
            j=mid-1
        else:
            i=mid+1

print("Last Occurance Position: {}".format(res))