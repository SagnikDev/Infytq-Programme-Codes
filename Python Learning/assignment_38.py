#PF-Assgn-38

def check_double(number):
    double=number*2
    number_list=list(str(number))
    num_len=len(number_list)
    number_list.sort()
    number_list=int("".join(number_list))
    double_list=list(str(double))
    double_len=len(double_list)
    double_list.sort()
    double_list=int("".join(double_list))
    if((num_len==double_len) and (number_list==double_list)):
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))