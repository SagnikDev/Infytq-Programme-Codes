n=4
table=[[None for i in range(n)] for j in range(n)]


num=1
for i in range(n):
    for j in range(n):
        table[i][j]=num
        num+=1

for i in table:
    print(i)

def go(i,j):
    if(i==n-1 and j==n-1):
        return table[i][j]
    ans=0
    if(i<n-1 and j<n-1):
        ans=table[i][j]+max(go(i,j+1),go(i+1,j))
    elif(i==n-1):
        ans=table[i][j]+go(i,j+1)
    else:
        ans=table[i][j]+go(i+1,j)
    return ans

print(go(0,0))