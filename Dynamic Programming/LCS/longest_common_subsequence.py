def lcs(x,y,n,m):
    if(m==0 or n==0):
        table[n][m]=0
        return table[n][m]
    elif (table[n][m] is not None):
        return table[n][m]
    elif (x[n-1]==y[m-1]):
        table[n][m]= 1+lcs(x,y,n-1,m-1)
        return table[n][m]
    else:
        table[n][m]= max(lcs(x,y,n,m-1),lcs(x,y,n-1,m))
        return table[n][m]

x="abcf"
y="abcdaf"
n=len(x)
m=len(y)
table=[[None for i in range(m+1)] for j in range(n+1)]
print(lcs(x,y,n,m))