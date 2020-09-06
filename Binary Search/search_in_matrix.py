arr=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
element=29
i=0
j=len(arr[0])-1

while(i>=0 and i<len(arr) and j>=0 and j<len(arr[0])):
    if(arr[i][j]==element):
        print(i,j)
        break
    else:
        if(arr[i][j]>element):
            j-=1
        elif(arr[i][j]<element):
            i+=1
        