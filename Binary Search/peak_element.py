arr=[10,20,15,2,23,90,67]

i=0
j=len(arr)-1
peak=-1
while(i<=j):
    mid=i+((j-i)//2)
    if(mid==0 and arr[mid]>=arr[mid+1]):
        peak=mid
        break
    if(mid==len(arr)-1 and arr[mid]>=arr[mid-1]):
        peak=mid
        break
    if(arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]):
        peak=mid
        break
    else:
        if(arr[mid]<arr[mid+1]):
            i=mid+1
        elif(arr[mid]<arr[mid-1]):
            j=mid-1

print(peak)