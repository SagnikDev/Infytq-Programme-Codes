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

x="acbcf"
y="abcdaf"
m=len(x)
n=len(y)
lcs_string=""
table=[[None for i in range(0,n+1)] for j in range(0,m+1)]

lcs(x,y,m,n)

for i in table:
    print(i)
lcs_string=""
while(m>0 or n>0):
    if(x[m-1]==y[n-1]):
        lcs_string+=x[m-1]
        m-=1
        n-=1
    else:
        if(table[m][n-1]>table[m-1][n]):
            lcs_string+=y[n-1]
            n-=1
        else:
            lcs_string+=x[m-1]
            m-=1
while(m>0):
    lcs_string+=x[m-1]
    m-=1
while(n>0):
    lcs_string+=y[n-1]
    n-=1

print("Shortest common Supersequence:")
print(lcs_string[::-1])