#PF-Assgn-46

def nearest_palindrome(number):
    #start writitng your code here
    while(number>0):
        if(palindrome(number)):
            return number
        else:
            number+=1
number=12300


def palindrome(number):
    num=number
    num_pal=0
    while(num>0):
        num_rem=num%10
        num_pal=(num_pal*10)+num_rem
        num=num//10
    if(num_pal==number):
        return True
    else:
        return False



print(nearest_palindrome(number))