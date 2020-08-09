arr=[2,3,5,6,8,10]
sum=10
#Knapsack Example
n=len(arr)
table=[[None for i in range(sum+1)] for j in range(n+1)]

#Initialize Table
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

for i in table:
    print(i)

if(table[n][sum]==True):
    print("Subset Sum present")