def count_subset(arr,sum):
    n=len(arr)
    table=[[None for i in range(sum+1)] for j in range(n+1)]
    #Initialize Table
    for row in range(0,n+1):
        for column in range(0,sum+1):
            if(row==0):
                table[row][column]=0
    for row in range(0,n+1):
        for column in range(0,sum+1):
            if(column==0):
                table[row][column]=1
    for row in range(1,n+1):
        for column in range(1,sum+1):
            if(arr[row-1]<=column):
                table[row][column]=table[row-1][column-arr[row-1]] + table[row-1][column]
            else:
                table[row][column]=table[row-1][column]

    for i in table:
        print(i)

    return table[n][sum]

def number_subset_with_diff(arr,diff):
    n=sum(arr)
    subset_sum_s1=(diff+n)//2
    return count_subset(arr,subset_sum_s1)


arr=[1,1,2,3]
diff=1

print(number_subset_with_diff(arr,diff))