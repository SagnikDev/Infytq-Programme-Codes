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
        table[i][j]=1+palindrome_partitioning(word,i,k)+palindrome_partitioning(word,k+1,j)
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