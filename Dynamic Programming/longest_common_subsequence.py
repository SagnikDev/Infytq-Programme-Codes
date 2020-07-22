word1="BATGGA"
word2="BYAXTXG"
# word1="Sa"
# word2="Sag"
column=len(word1)+2
row=len(word2)+2
table = [[None for i in range(column)] for j in range(row)]

word1=[i for i in word1]
word2=[i for i in word2]


for i in range(2,row-1):
    table[0][i]=word1.pop()
for i in range(2,column+1):
    table[i][0]=word2.pop()

table[1]=[0]*column
for i in range(0,column+1):
    table[i][1]=0

for i in range(2,column+1):
    for j in range(2,row-1):
        if(table[i][0]==table[0][j]):
            table[i][j]=table[i-1][j-1]+1
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])

print("The longest common subsequence: "+str(table[i][j]))
print()
print("The Table:")
for i in table:
    print(i)
print("Row: "+str(len(table)))
print("Column: "+str(len(table[0])))

