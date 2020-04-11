#PF-Assgn-48

def find_correct(word_dict):
    correct=0
    almost_correct=0
    wrong=0
    #start writing your code here
    arr_correct=[]
    arr_wrong=[]
    for i in word_dict:
        arr_correct.append(i)
        arr_wrong.append(word_dict[i])
    for i in range(len(arr_correct)):
        flag=words_check(arr_correct[i],arr_wrong[i])
        if(flag=='w'):
            wrong+=1
        elif(flag=='a'):
            almost_correct+=1
        else:
            correct+=1
    return [correct,almost_correct,wrong]

def words_check(word1,word2):
    count=0
    if(len(word1)!=len(word2)):
        return 'w'
    w1=[i for i in word1]
    w2=[i for i in word2]
    for i in range(len(w1)):
        if(w1[i]!=w2[i]):
            count+=1
    if(count>2):
        return 'w'
    elif(count>0):
        return 'a'
    else:
        return 'c'

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))