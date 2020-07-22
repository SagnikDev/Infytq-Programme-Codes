sequence=[10,22,9,33,21,50,41,60,10,22,9,33,21,50,41,60,10,22,9,33,21,50,41,60,70,10,40,90]

lis_arr={}
for i in sequence:
    lis_arr[i]=1

for i in range(1,len(sequence)):
    for j in range(0,len(sequence)):
        if(sequence[j]<sequence[i]):
            lis_arr[sequence[i]]=max(lis_arr[sequence[i]],lis_arr[sequence[j]]+1)
print(lis_arr[sequence[len(sequence)-1]])