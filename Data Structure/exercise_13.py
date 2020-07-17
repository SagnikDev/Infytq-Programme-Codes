#DSA-Tryout
import random
def find_it(num,element_list):
    count=0
    low=0
    high=len(element_list)-1
    mid=0

    while(True):
        mid=(high+low)//2
        count+=1
        if(element_list[mid]==num):
            return count
        elif(element_list[mid]>num):
            high=mid-1
        elif(element_list[mid]<num):
            low=mid+1

#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    element_list=initialize_list_of_elements(n)
    random_no=random.randint(1,n)
    total_guess=find_it(random_no,element_list)
    print(total_guess)


#Pass different values to play() and observe the output
play(400)