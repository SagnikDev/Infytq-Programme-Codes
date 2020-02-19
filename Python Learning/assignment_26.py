#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    legs_half=legs/2
    rabbit_count_test=legs_half-heads
    chicken_count_test=heads-rabbit_count_test
    if((rabbit_count_test*4+chicken_count_test*2==legs) and (rabbit_count_test>=0 and chicken_count_test>=0)):
        rabbit_count=rabbit_count_test
        chicken_count=chicken_count_test
        print(int(chicken_count),int(rabbit_count))
    else:
        print(error_msg)
    #Populate the variables: chicken_count and rabbit_count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(23,67)