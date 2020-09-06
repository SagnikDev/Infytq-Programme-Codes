arr=[5,10,30,20,40]
element=20
i=0
j=len(arr)-1
res=-1
while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
      res=mid
      break
    if(mid-1>=i and arr[mid-1]==element):
        res=mid-1
        break
    if(mid+1<=j and arr[mid+1]==element):
        res=mid+1
        break
    if(arr[mid]>element):
        j=mid-2
    else:
        i=mid+2

print(res)