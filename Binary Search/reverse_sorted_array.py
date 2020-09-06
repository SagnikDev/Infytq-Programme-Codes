arr=[32,31,30,29,28,27,26,25,24]
i=0
j=len(arr)-1
element=24

def search(arr,i,j,element):
    if(i>j):
        return -1
    mid=i+((j-i)//2)
    # print(arr[mid])
    if(arr[mid]==element):
        return mid
    if(arr[mid]>element):
        i=mid+1
    else:
        j=mid-1
    return search(arr,i,j,element)


print(search(arr,i,j,element))