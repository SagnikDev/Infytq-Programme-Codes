#DSA-Exer-18

def find_next_min(num_list,start_index):
    min=num_list[start_index]
    index=start_index
    for i in range(start_index+1,len(num_list)):
        if(num_list[i]<min):
            min=num_list[i]
            index=i
    return index
    

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=0
print("Index of the next minimum element is", find_next_min(num_list,start_index))