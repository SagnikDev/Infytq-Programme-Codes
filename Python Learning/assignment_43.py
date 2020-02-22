def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(1,(num+1)):
        if(num%i==0):
            factors.append(i)
    return len(factors)
#PF-Assgn-43

def find_smallest_number(num):
    factors=0
    number=1
    while(factors!=num):
        factors=find_factors(number)
        number+=1
    return number-1

    
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)