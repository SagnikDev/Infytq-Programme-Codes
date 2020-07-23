def go(src,dest,n):
    if(n==0):
        if(src==dest):
            return 1
        return 0
    ans=0
    for i in range(0,3):
        if(i==src):
            continue
        else:
            ans+=1+go(i,dest,n-1)
    return ans



print(go(3,3,1))