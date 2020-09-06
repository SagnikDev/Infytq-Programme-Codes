arr=[4,6,10]
element=7
i=0
j=len(arr)-1

floor=-1
ceil=-1

while(i<=j):
    mid=i+((j-1)//2)
    if(arr[mid]==element):
        floor=mid
    else:
        if(arr[mid]<element):
            floor=mid
            i=mid+1
        elif(arr[mid]>element):
            j=mid-1
i=0
j=len(arr)-1

while(i<=j):
    mid=i+((j-1)//2)
    if(arr[mid]==element):
        ceil=mid
    else:
        if(arr[mid]<element):
            i=mid+1
        elif(arr[mid]>element):
            ceil=mid
            j=mid-1
minm=min(abs(element-arr[floor]),abs(element-arr[ceil]))

print(minm)