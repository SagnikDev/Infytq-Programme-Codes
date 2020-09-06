arr=[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
i=0
j=1

while(arr[j]==0):
    i=j
    j=j*2
res=-1
while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==1):
        res=mid
        j=mid-1
    # elif(arr[mid]>1):
    #     j=mid-1
    elif(arr[mid]<1):
        i=mid+1

print(res)