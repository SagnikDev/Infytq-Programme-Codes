#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum_ON=0
    if (filter_func==None):
        return sum(list_of_num)
    for i in list_of_num:
        if(filter_func(i)):
            sum_ON+=i
    return sum_ON




odd=(lambda x: x%2==1)

even=(lambda x: x%2==0)


sample_data=[x for x in range(1,11)]

print(sum_of_numbers(sample_data,None))
