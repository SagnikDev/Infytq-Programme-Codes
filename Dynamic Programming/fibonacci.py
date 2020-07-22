# def fibonacci(n):
#     if(n<=1):
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(40))

'''
There having two properties:
1.Optimal Substructure
2.Overlapping Subproblem

Sollution:
-Memoization
-Tabulation
'''
#Memoization--Creating a lookup table
# table=[-1]*1000000

# def fibonacci(n):
#     if(n<=1):
#         return n
#     elif(table[n]>-1):
#         return table[n]
#     else:
#         table[n]=fibonacci(n-1)+fibonacci(n-2)
#         return table[n]

# print(fibonacci(40))

#Tabulation Method
def fibonacci(n):
    table=[0]*(100)
    table[0]=0
    table[1]=1

    for i in range(2,n+1):
        table[i]=table[i-1]+table[i-2]
    print(table[n])
fibonacci(40)
