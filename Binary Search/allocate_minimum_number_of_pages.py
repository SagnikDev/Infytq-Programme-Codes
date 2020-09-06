arr=[10,20,30,40]
k=2
res=-1

def isValid(arr,k,mid):
    student=1
    sump=0
    for i in arr:
        sump+=i
        if(sump>mid):
            student+=1
            sump=i
        if(student>k):
            return False
    return True

if(k>len(arr)):
    print("False")
else:
    start=max(arr)
    end=sum(arr)
    while(start<=end):
        mid=start+((end-start)//2)
        if(isValid(arr,k,mid)==True):
            res=mid
            end=mid-1
        else:
            start=mid+1

print(res)