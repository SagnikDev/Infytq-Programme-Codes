arr=[1,2,3,4,5,6,7,8]
i=0
j=len(arr)-1
element=7
def binary_search(arr,i,j,element):
    if(i>j):
        return -1
    # mid=(i+j)//2
    mid=i+((j-i)//2)
    if(arr[mid]==element):
        return mid
    if(arr[mid]>element):
        j=mid-1
    else:
        i=mid+1
    return binary_search(arr,i,j,element)    


print(binary_search(arr,i,j,element))