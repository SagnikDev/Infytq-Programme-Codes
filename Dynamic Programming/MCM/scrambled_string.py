def solve(a,b):
    for i in range(0,len(table)):
        if(table[i][0]==a+" "+b):
            return table[i][1]
    key=a+" "+b
    if(a==b):
        return True
    if(len(a)<=1):
        return False
    flag=False
    n=len(a)
    for i in range(1,n):
        if((solve(a[:i],b[-i:])==True and solve(a[i:],b[:-i])==True) or (solve(a[:i],b[:i])==True and solve(a[i:],b[i:])==True)):
            flag=True
            break
    table.append([key,flag])
    return flag




if __name__ == "__main__":
    a="great"
    b="rgeat"
    global table
    table=[[None for i in range(2)] for j in range(1)]
    if(len(a) is not len(b)):
        print("False")
    elif (len(a)==0 and len(b)==0):
        print("True")
    else:
        print(solve(a,b))
    for i in table:
        print(i)