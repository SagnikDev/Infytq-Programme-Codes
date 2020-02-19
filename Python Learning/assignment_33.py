#PF-Assgn-33

def find_common_characters(msg1,msg2):
    msg1=set(msg1)
    msg1=list(msg1)
    if(" " in msg1):
        msg1.pop(msg1.index(" "))
    msg2=set(msg2)
    msg2=list(msg2)
    if(" " in msg2):
        msg2.pop(msg2.index(" "))
    list1=[]
    for i in msg1:
        if i in msg2:
            list1.append(i)
    if(len(list1)>0):
        return "".join(list1)
    else:
        return -1
#Provide different values for msg1,msg2 and test your program
msg1="Python"
msg2="python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)