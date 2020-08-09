def josephus(array,index,k):
    if(len(array)==1):
        return array[0]
    else:
        index=(index+k)%len(array)
        array.remove(array[index])
        return josephus(array,index,k)



n=40
k=7
index=0
array=[i for i in range(1,41)]


print(josephus(array,index,k-1))