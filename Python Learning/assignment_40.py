#PF-Assgn-40
def palindrome_re(word):
    if(len(word)==1):
        return word
    return word[len(word)-1]+palindrome_re(word[:-1])

def is_palindrome(word):
    if(len(word)==0):
        return True
    elif(word==palindrome_re(word)):
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("Sagnik")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")