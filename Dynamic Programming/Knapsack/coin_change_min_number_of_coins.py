import sys
coins=[1,2,3]
sum=6
n=len(coins)
table=[[None for i in range(sum+1)] for j in range(n+1)]

for row in range(0,n+1):
    for column in range(0,sum+1):
        if(column==0):
            table[row][column]=1
        if(row==0):
            table[row][column]=sys.maxsize-1
for column in range(1,sum+1):
    if(column%coins[0]==0):
        table[1][column]=column//coins[0]
    else:
        table[1][column]=sys.maxsize-1

for row in range(2,n+1):
    for column in range(1,sum+1):
        if(coins[row-1]<=column):
            table[row][column]=min(1+table[row][column-coins[row-1]],table[row-1][column])
        else:
            table[row][column]=table[row-1][column]

for i in table:
    print(i)