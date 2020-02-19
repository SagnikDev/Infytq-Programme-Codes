#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    sum=0
    list_sides=[num1,num2,num3]
    for i in range(0,len(list_sides)):
        for j in range(0,len(list_sides)):
            if(j==i):
                continue
            else:
                sum=sum+list_sides[j]
        if(sum<=list_sides[i]):
            return failure
            break
        else:
            sum=0
    return success
    # #Use the following messages to return the result wherever necessary
    # return success
    # return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))