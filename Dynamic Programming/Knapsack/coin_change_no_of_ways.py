coins=[1,2,3]
sum=5
n=len(coins)
table=[[None for i in range(sum+1)] for j in range(n+1)]

for row in range(0,n+1):
    for column in range(0,sum+1):
        if(row==0):
            table[row][column]=0
        if(column==0):
            table[row][column]=1

for row in range(1,n+1):
    for column in range(1,sum+1):
        if(coins[row-1]<=column):
            table[row][column]=table[row][column-coins[row-1]]+table[row-1][column]
        else:
            table[row][column]=table[row-1][column]

for i in table:
    print(i)
print("Number of ways:")
print(table[n][sum])