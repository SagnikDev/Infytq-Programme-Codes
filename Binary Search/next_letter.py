arr=['a','c','f','h']
element='f'
i=0
j=len(arr)-1
res="#"

while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        i=mid+1
    elif(arr[mid]>element):
        res=mid
        j=mid-1
    elif(arr[mid]<element):
        i=mid+1

print(res)