#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count=0
    average=sum(list_of_marks)/len(list_of_marks)
    for i in list_of_marks:
        if(i>average):
            count+=1
    return (count*100/len(list_of_marks))

def sort_marks():
    list_of_marks1=list(list_of_marks)
    list_of_marks1.sort()
    return list_of_marks1
def generate_frequency():
    marks=[0]*26
    for i in list_of_marks:
        marks[i]+=1
    return marks
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())