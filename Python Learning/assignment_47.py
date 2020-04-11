#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    sentence=sentence.split(" ")
    for i in sentence[0::2]:
        sentence[sentence.index(i)]=i[::-1]
    for i in sentence[1::2]:
        sentence[sentence.index(i)]=encrypt(i)
    return ' '.join(sentence)


def encrypt(a):
    arr=[]
    vowel_collect=[]
    vowel=['a','e','i','o','u']
    for i in a:
        arr.append(i)
    arr2=arr.copy()
    for i in arr:
        if i in vowel:
            vowel_collect.append(i)
            arr2.remove(i)
    for i in vowel_collect:
        arr2.append(i)
    return ''.join(arr2)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)


#eht snu sesir ni eht stea