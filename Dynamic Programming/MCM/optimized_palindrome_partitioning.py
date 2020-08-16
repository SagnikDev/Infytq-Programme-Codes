import sys
def isPalindrome(word,i,j):
    word=word[i:j+1]
    if(word==word[::-1]):
        return True
def palindrome_partitioning(word,i,j):
    if(table[i][j] is not None):
        return table[i][j]
    if(i>=j):
        table[i][j]=0
        return table[i][j]
    if(isPalindrome(word,i,j)==True):
        return 0
    mn=sys.maxsize
    for k in range(i,j):
        if(table[i][k] is not None):
            left=table[i][k]
        else:
            left=palindrome_partitioning(word,i,k)
            left=table[i][k]
        if(table[k+1][j] is not None):
            right=table[k+1][j]
        else:
            table[k+1][j]=palindrome_partitioning(word,k+1,j)
            right=table[k+1][j]
        table[i][j]=1+left+right
        temp=table[i][j]
        mn=min(temp,mn)
    return mn


word="sagnik"
i=0
j=len(word)-1
table=[[None for _ in range(j+1)] for x in range(j+1)]
print(palindrome_partitioning(word,i,j))

for i in table:
    print(i)