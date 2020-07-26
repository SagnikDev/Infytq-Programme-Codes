def knapsack(wt,val,w,n):
    if(w<=0 or n==0):
        return 0
    elif(dp[w][n]>-1):
        return dp[w][n]
    elif(w>=wt[n-1]):
        dp[w][n]=max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return dp[w][n]
    elif(w<wt[n-1]):
        dp[w][n]=knapsack(wt,val,w,n-1)
        return dp[w][n]


wt=[1,2,3,4,5]
val=[1,10,4,5,7]
w=7
n=len(wt)
dp=[[-1 for i in range(n+1)] for j in range(w+1)]

print(knapsack(wt,val,w,n))