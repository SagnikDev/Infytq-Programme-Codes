#PF-Assgn-56
import re
def max_frequency_word_counter(data):
    word=""
    words=[]
    frequency=0
    compiler=re.compile(r"\s(\w*)")
    collection=compiler.findall(data)
    frequency_measure={}
    for i in collection:
        if(i in frequency_measure):
            frequency_measure[i]+=1
        else:
            frequency_measure[i]=1
    frequency=max(list(frequency_measure.values()))  
    for i in frequency_measure:
        if(frequency_measure.get(i)==frequency):
            words.append(i)
    prev=0
    for i in words:
        if len(i)>prev:
            prev=len(i)
            word=i
            
    print(word)
    print(frequency)


#Provide different values for data and test your program.
data="Hands to clap and eyes to see"
max_frequency_word_counter(data)