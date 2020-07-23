value=[60,100,120]
weight=[10,20,30]
w=50
n=len(value)

table=[[-1 for i in range(n+1)] for j in range(w+1)]

def knapsack(w,weight,value,n):
    if(table[w][n]>-1):
        return table[w][n]
    elif(w==0 or n==0):
        table[w][n]=0
        return table[w][n]
    elif(weight[n-1]>w):
        table[w][n]= knapsack(w,weight,value,n-1)
        return table[w][n]
    else:
        table[w][n]= max(value[n-1]+knapsack(w-weight[n-1],weight,value,n-1),knapsack(w,weight,value,n-1))
        return table[w][n]



print(knapsack(w,weight,value,n))