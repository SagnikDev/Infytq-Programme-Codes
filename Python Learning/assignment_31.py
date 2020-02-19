#PF-Assgn-31
def check_palindrome(word):
    temp=word[::-1]
    if(word==temp):
        return True
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")