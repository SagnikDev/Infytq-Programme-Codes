#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    data=data.split(" ")
    encoded_list=[]
    for i in data:
        a=sms_encryption(i)
        if(len(a)==0):
            return ""
        encoded_list.append(a)
    return ' '.join(encoded_list)

def sms_encryption(word):
    vowels=['a','e','i','o','u']
    if((len(word)==1) and (word.lower() in vowels)):
        return word
    word=[i for i in word]
    word2=word.copy()
    for i in word:
        if(i.lower() in vowels):
            word2.remove(i)
    return ''.join(word2)



data="MSD says I love cricket and tennis too"
# data="I love Python"
print(sms_encoding(data))