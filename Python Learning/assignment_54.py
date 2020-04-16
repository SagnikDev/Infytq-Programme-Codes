#PF-Assgn-54
def check_anagram(data1,data2):
    #start writing your code here
    data1=[i.lower() for i in data1]
    data2=[i.lower() for i in data2]

    if(len(data1)!= len(data2)):
        return False
    a=data1.copy()
    b=data2.copy()
    a.sort()
    b.sort()
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return False
    for i in range(len(data1)):
        if(data1[i]==data2[i]):
            return False

    return True



print(check_anagram("About", "table"))