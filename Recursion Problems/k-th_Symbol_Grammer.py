#Kth Symbol o Grammer

# def find(n,k):
#     if(n==1):
#         return 0
#     if(k%2==0):
#         ans=find(n-1,(k/2))
#         if(ans==1):
#             return 0
#         else:
#             return 1
#     else:
#         return find(n-1,(k/2))

#Next sollution

def find (n,k):
    if(n==1):
        return 0
    mid=(2**(n-1)//2)
    if(k<=mid):
        return find(n-1,k)
    else:
        ans=find(n-1,k-mid)
        if(ans==1):
            return 0
        else:
            return 1


n=4
k=5
print(find(n,k))