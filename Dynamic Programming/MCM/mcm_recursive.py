import sys
def mcm(arr,i,j):
    if(table[i][j] is not None):
        return table[i][j]
    if(i>=j):
        table[i][j]=0
        return table[i][j]
    min_answr=sys.maxsize
    for k in range(i,j):
        table[i][j]=mcm(arr,i,k)+mcm(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        temp_answr=table[i][j]
        min_answr=min(min_answr,temp_answr)
    return min_answr

arr=[40,20,30,10,30]
i=1
j=len(arr)-1
table=[[None for _ in range(j+1)] for x in range(j+1)]
print(mcm(arr,i,j))