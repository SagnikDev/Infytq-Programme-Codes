#PF-Assgn-44

def find_duplicates(list_of_numbers):
    duplicate_list=[]
    #start writing your code here
    for i in list_of_numbers:
        list_of_numbers.remove(i)
        if i in list_of_numbers:
            duplicate_list.append(i)
            list_of_numbers.remove(i)
    return (duplicate_list)
list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)