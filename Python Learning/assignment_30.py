#PF-Assgn-30

def encode(message):
    sets=list(message)
    prev=sets[0]
    counter=1
    list2=[]
    for i in range(1,len(message)):
        if(message[i]==prev):
            counter+=1
            prev=message[i]
        else:
            list2.append(counter)
            list2.append(prev)
            counter=1
            prev=message[i]
    list2.append(counter)
    list2.append(prev)
    list2=map(str,list2)
    list2="".join(list2)
    return list2
    #Remove pass and write your logic here
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCABBB")
print(encoded_message)