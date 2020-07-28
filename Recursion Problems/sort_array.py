def put(array,temp):
    if(len(array)==0 or array[-1]<=temp):
        array.append(temp)
        return array
    last=array[-1]
    arr=put(array[:-1],temp)
    arr.append(last)
    return arr

def demo_sort(array):
    if(len(array)==1):
        return array
    last=array[-1]
    arr=demo_sort(array[:-1])
    return put(arr,last)

array=[2,3,7,6,4,5,9]
print(demo_sort(array))