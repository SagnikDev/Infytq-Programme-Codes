
def min_subset_diff(arr,sum):
    n=len(arr)
    table=[[None for i in range(sum+1)] for j in range(n+1)]

    for row in range(0,n+1):
        for column in range(0,sum+1):
            if(row==0):
                table[row][column]=False
    for row in range(0,n+1):
        for column in range(0,sum+1):
            if(column==0):
                table[row][column]=True
    for row in range(1,n+1):
        for column in range(1,sum+1):
            if(arr[row-1]<=column):
                table[row][column]=(table[row-1][column-arr[row-1]] or table[row-1][column])
            else:
                table[row][column]=table[row-1][column]

    candidates=[]
    for column in range(0,(sum//2)+1):
        if(table[n][column]==True):
            candidates.append(column)
    minimum=100
    for i in candidates:
        minimum=min(minimum,sum-2*i)


    for i in table:
        print(i)
    return (minimum)


arr=[1,2,7]
sum=sum(arr)
print(min_subset_diff(arr,sum))