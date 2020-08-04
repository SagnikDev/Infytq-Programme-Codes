length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
n=8


table=[[None for i in range(n+1)] for j in range(n+1)]

for row in range(0,n+1):
    for column in range(0,n+1):
        if(row==0 or column==0):
            table[row][column]=0

for row in range(1,n+1):
    for column in range(1,n+1):
        if(length[row-1]<=column):
            table[row][column]=max(price[row-1]+table[row][column-length[row-1]],table[row-1][column])
        else:
            table[row][column]=table[row-1][column]

for i in table:
    print(i)


print("Maximum price:")
print(table[n][n])