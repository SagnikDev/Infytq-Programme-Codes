#PF-Assgn-41
def find_ten(number):
    if(len(number)==0):
        return 0
    return int(number[0])+find_ten(number[1:])

def find_ten_substring(num_str):
    arr=[]
    list1=list(num_str[i:j+1] for i in range (len(num_str)) for j in range(i,len(num_str)))
    for i in list1:
        result=find_ten(i)
        if(result==10):
            arr.append(i)
    return (arr)
    
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
