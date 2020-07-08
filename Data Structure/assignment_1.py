#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    list3=[]
    list2=list2[::-1]
    for i in range(0,len(list2)):
        if list1[i]==None:
            list1[i]=""
        if list2[i]==None:
            list2[i]=""
        list3.append(list1[i]+list2[i])
    return (" ".join(list3))
    #write your logic here
    # return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)