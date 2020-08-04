wt=[1,2,3,4,5]
val=[1,10,4,5,7]
w=7
n=len(wt)
table=[[None for i in range(w+1)] for j in range(n+1)]
for i in table:
    print(i)
for row in range(0,n+1):
    for column in range(0,w+1):
        if(row==0 or column==0):
            table[row][column]=0
for row in range(1,n+1):
    for column in range(1,w+1):
        if(wt[row-1]<=column):
            table[row][column]=max(val[row-1]+table[row-1][column-wt[row-1]],table[row-1][column])
        else:
            table[row][column]=table[row-1][column]
 
print(table[n][w])
for i in table:
    print(i)
# print(knapsack(wt,val,w,n))