#DSA-Exer-24

# def make_change(denomination_list, amount):
#     changes=[]
#     while(amount>0):
#         denomination_list.sort(reverse=True)
#         for i in denomination_list:
#             if(i<=amount):
#                 changes.append(i)
#                 amount-=i
#                 break
#     print(changes)

max=1000
table=[-1]*max
def make_change(denomination_list,amount):
    if(table[amount]>-1):
        return table[amount]
    elif(amount<=0):
        table[amount]=0
        return table[amount]
    for i in range(0,len(denomination_list)):
        if(denomination_list[i]<=amount):
            table[amount]=1+make_change(denomination_list,amount-denomination_list[i])
            res_test=table[amount]
            if(res_test < max and res_test !=max):
                table[amount]=res_test
    return table[amount]

    


#Pass different values to the function and test your program
amount=500
denomination_list = [1,15,10]
# m=len(denomination_list)

print(make_change(denomination_list, amount))