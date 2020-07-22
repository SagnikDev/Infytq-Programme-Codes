word1="TRAC"
word2="HCRAM"
word1=[i for i in word1]
word2=[i for i in word2]

row=len(word1)+2
column=len(word2)+2

table = [[None for i in range(column)] for j in range(row)]
table[0][0]=0

for i in range(2,row):
    table[i][0]=word1.pop()
for i in range(2,column):
    table[0][i]=word2.pop()

for i in range(1,column):
    table[1][i]=i-1
for i in range(1,row):
    table[i][1]=i-1
# table[1]=[i for i in range(column)]
# for i in range(0,row):
#     table[i][1]=0

for i in range(2,row):
    for j in range(2,column):
        if(table[i][0]==table[0][j]):
            table[i][j]=table[i-1][j-1]
        else:
            table[i][j]=min(table[i-1][j-1],table[i][j-1],table[i-1][j])+1

print("The edit distance is: "+str(table[i][j]))
for i in table:
    print(i)