def solve(s,i,j,is_true):
    if(is_true==True):
        t=1
    else:
        t=0
    
    if(table[t][i][j] is not None):
        return table[t][i][j]
    if(i>j):
        return 0

    if(i==j):
        if(is_true==True):
            if(s[i]=="T"):
                return 1
            else:
                return 0
        else:
            if(s[i]=="F"):
                return 1
            else:
                return 0
    ans=0
    for k in range(i+1,j,2):
        table[1][i][k-1]=solve(s,i,k-1,True)
        LT=table[1][i][k-1]
        # table.append([str(i)+"_"+str(k-1)+"_"+str(True),LT])
        table[0][i][k-1]=solve(s,i,k-1,False)
        LF=table[0][i][k-1]
        # table.append([str(i)+"_"+str(k-1)+"_"+str(False),LF])
        table[1][k+1][j]=solve(s,k+1,j,True)
        RT=table[1][k+1][j]
        # table.append([str(k+1)+"_"+str(j)+"_"+str(True),RT])
        table[0][k+1][j]=solve(s,k+1,j,False)
        RF=table[0][k+1][j]
        # table.append([str(k+1)+"_"+str(j)+"_"+str(False),RF])

        if(s[k]=="&"):
            if(is_true==True):
                ans+=LT*RT
            else:
                ans+=LF*RF+LT*RF+LF*RT
        if(s[k]=="|"):
            if(is_true==True):
                ans+=LT*RT+LT*RF+LF*RT
            else:
                ans+=LF*RF
        if(s[k]=="^"):
            if(is_true==True):
                ans+=LT*RF+LF*RT
            else:
                ans+=LF*RF+LT*RT
    return ans


s="T|F&T^F&T|F&T^F|F&T^F|T|F&T^F^T|F&T^F^T|F&T^F&T|F&T^F|F&T^F|T|F&T^F^T|F&T^F&T|F&T^F&T|F&T^F|F&T^F|T|F&T^F^T|F&T^F"
i=0
j=len(s)-1
table=[[[None for column in range(j+1)]for row in range(j+1)]for dim in range(2)]

print(solve(s,i,j,True))