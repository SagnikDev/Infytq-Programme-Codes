x="abcfxs"
y="adcfxq"
m=len(x)
n=len(y)

table=[[None for i in range(0,n+1)] for j in range(0,m+1)]

for row in range(0,m+1):
    for column in range(0,n+1):
        if(row==0 or column==0):
            table[row][column]=0

for row in range(1,m+1):
    for column in range(1,n+1):
        if(x[row-1]==y[column-1]):
            table[row][column]=1+table[row-1][column-1]
        else:
            table[row][column]=0
for i in table:
    print(i)

print("The longest Substring:")
maxn=0
for i in table:
    maxn=max(max(i),maxn)
print(maxn)