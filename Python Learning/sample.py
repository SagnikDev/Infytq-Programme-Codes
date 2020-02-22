#PF-Exer-32

def human_pyramid(no_of_people):
    if(no_of_people==1):
        return 1*(50)
    else:
        return no_of_people*(50)+human_pyramid(no_of_people-2)

def find_maximum_people(max_weight):
    if(max_weight<=50):
        return 0
    people=1
    while(max_weight>=human_pyramid(people)):
        people+=2
    return people-2
#Provide different values for max_weight and test your program
max_people=find_maximum_people(1250)
print(max_people)