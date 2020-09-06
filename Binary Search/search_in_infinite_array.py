arr=[i+10 for i in range(3,20)]
element=22
i=0
j=1
res=-1
while(element>arr[j]):
    i=j
    j=j*2

while(i<=j):
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        res=mid
        break
    elif(arr[mid]>element):
        j=mid-1
    elif(arr[mid]<element):
        i=mid+1

print(res)