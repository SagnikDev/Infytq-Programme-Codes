arr=[1,2,3,4,8,10,10,12,19]
i=0
j=len(arr)-1
res=-1
element=9

while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        res=mid
        break
    elif(arr[mid]<element):
        i=mid+1
    elif(arr[mid]>element):
        res=mid
        j=mid-1

print(res)