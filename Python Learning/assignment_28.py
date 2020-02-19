#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    list_nums=[]
    num_char=""
    if(num1<num2):
        for i in range(num1,num2+1):
            num_char=str(i)
            if(len(num_char)>2):
                continue
            if(((i/10)+(i%10))%3==0):
                if(i%5==0):
                    list_nums.append(i)
    else:
        return -1
    if(list_nums):
        max_num=max(list_nums)     
    else:
        return -1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)