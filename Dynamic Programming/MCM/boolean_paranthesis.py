def solve(s,i,j,isTrue):
    if(i>j):
        return False
    if(i==j):
        if(isTrue==True):
            return s[i]=="T"
        else:
            return s[i]=="F"
    ans=0
    for k in range(i+1,j,2):
        LT=solve(s,i,k-1,True)
        LF=solve(s,i,k-1,False)
        RT=solve(s,k+1,j,True)
        RF=solve(s,k+1,j,False)

        if(s[k]=="&"):
            if(isTrue==True):
                ans=ans+(LT*RT)
            else:
                ans=ans+(LF*RT+LT*RF+LF*RF)
        if(s[k]=="|"):
            if(isTrue==True):
                ans=ans+(LT*RT+LF*RT+LT*RF)
            else:
                ans=ans+(LF*RF)
        if(s[k]=="^"):
            if(isTrue==True):
                ans=ans+(LF*RT+LT*RF)
            else:
                ans=ans+(LT*RT+LF*RF)   
string="T|F&T^F"
i=0
j=len(string)-1
print(solve(string,i,j,True))