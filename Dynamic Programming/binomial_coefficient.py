#Binomial Coefficient
#MEMOIZATION
def coeff(n,k):
    if(table[n][k]>-1):
        return table[n][k]
    elif(k==0 or k==n):
        table[n][k]=1
        return 1
    else:
        table[n][k]=coeff(n-1,k-1)+coeff(n-1,k)
        return table[n][k]

row=100
column=100
table=[[-1 for i in range (column)]for j in range(row)]

print(coeff(50,30))

# TABULAR 

