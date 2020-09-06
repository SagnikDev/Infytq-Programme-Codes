arr=[18,2,5,6,8,11,12,15]
n=len(arr)
i=0
j=len(arr)-1
res=-1
if(arr[i]<=arr[j]):
    res=i
else:
    while(i<=j):
        mid=i+((j-i)//2)
        next=(mid+1)%n
        previous=(mid+n-1)%n
        if(arr[mid]<=arr[previous] and arr[mid]<=arr[next]):
            res=mid
            break
        else:
            if(arr[i]<arr[mid]):
                i=mid+1
            elif (arr[mid]<arr[j]):
                j=mid-1
print(res)