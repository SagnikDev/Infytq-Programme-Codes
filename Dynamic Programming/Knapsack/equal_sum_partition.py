def subset_sum(arr,sum):
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
                table[row][column]=table[row-1][column-arr[row-1]] or table[row-1][column]
            else:
                table[row][column]=table[row-1][column]
    return table[n][sum]


arr=[5,1,11,5]
if(sum(arr)%2!=0):
    print("Not Possible")
else:
    res=subset_sum(arr,sum(arr)//2)
    if(res==True):
        print("Possible")
    else:
        print("Not Possible")