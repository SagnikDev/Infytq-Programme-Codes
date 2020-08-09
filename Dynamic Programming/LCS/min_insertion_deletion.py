def lcs(x,y,m,n):
    for row in range(0,m+1):
        for column in range(0,n+1):
            if(row==0 or column==0):
                table[row][column]=0
    for row in range(1,m+1):
        for column in range(1,n+1):
            if(x[row-1]==y[column-1]):
                table[row][column]=1+table[row-1][column-1]
            else:
                table[row][column]=max(table[row][column-1],table[row-1][column])


x="heap"
y="pea"
m=len(x)
n=len(y)
lcs_string=""
table=[[None for i in range(0,n+1)] for j in range(0,m+1)]

lcs(x,y,m,n)

for i in table:
    print(i)

lcs_num=table[m][n]

print("Min No of deletion:")
print(m-lcs_num)
print("Min no of insertion:")
print(n-lcs_num)