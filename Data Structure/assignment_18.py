#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    text=text.split(" ")
    unknown_words=[]
    for i in text:
        if(i not in vocabulary):
            if(i not in unknown_words):
                unknown_words.append(i)
    if(len(unknown_words)==0):
        return -1
    else:
        return unknown_words

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary =["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)