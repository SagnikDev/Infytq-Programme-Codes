import time
# starting time
start = time.time()
import sys
def solve(e,f):
    if(table[e][f] is not None):
        return table[e][f]
    if(f==0 or f==1):
        return f
    if(e==1):
        return f
    mn=sys.maxsize
    for k in range(1,f+1):
        if(table[e-1][k-1] is not None):
            left=table[e-1][k-1]
        else:
            left=solve(e-1,k-1)
            table[e-1][k-1]=left
        if(table[e][f-k] is not None):
            right=table[e][f-k]
        else:
            right=solve(e,f-k)
            table[e][f-k]=right
        temp=1+max(left,right)
        mn=min(mn,temp)
    table[e][f]=mn
    return mn

#Starting Code
eggs=3
floor=10
table=[[None for i in range(floor+1)] for j in range(eggs+1)]
print(solve(eggs,floor))

for i in table:
    print(i)

end = time.time()
# total time taken
print(f"Runtime of the program is {end - start}")