#DSA-Tryout

import random

def find_it(num,element_list):
    count=0
    for i in element_list:
        count+=1
        if(i==num):
            return count
    #Remove pass and write the logic to search num in element_list using linear search algorithm
    #Return the total number of guesses made 

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    list_of_elements=list_of_elements[::-1]
    return list_of_elements

def play(n):
    element_list=initialize_list_of_elements(n)
    random_no=random.randint(1,n)
    total_guess=find_it(random_no,element_list)
    print(total_guess)
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.

#Pass different values to play() and observe the output
play(400)