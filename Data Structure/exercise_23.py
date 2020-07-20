#DSA-Exer-23

def arrange_tickets(tickets_list):
    slist=["T"+str(i) for i in range(1,21)]
    list2=[]
    for i in slist:
        if(i in tickets_list):
            list2.append(i)
        else:
            list2.append("V")
    group1=list2[0:10]
    group2=list2[10:]
    while("V" in group2):
        group2.remove("V")
    for i in range(0,len(group1)):
        if(group1[i] is "V"):
            group1[i]=group2[0]
            group2.remove(group2[0])
    return group1

tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
