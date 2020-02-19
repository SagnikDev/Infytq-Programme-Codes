#PF-Assgn-36
def create_largest_number(number_list):
    largest_number=[]
    for i in range(0,len(number_list)):
        num=max(number_list)
        number_list.remove(num)
        largest_number.append(str(num))
    largest_number="".join(largest_number)
    return int(largest_number)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)