#DSA-Assgn-19

def last_instance( num_list,  start,  end,  key):
    if(key in num_list):
        a=end
        while(a>start):
            if(num_list[a]==key):
                return a
            a-=1
    else:
        return -1

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=4 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")