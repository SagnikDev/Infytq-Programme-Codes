sets={""}
def subset(word,output):
    if(word==""):
        sets.add(output)
        # print(output)
    else:
        output1=output+word[0]
        output2=output
        subset(word[1:],output1)
        subset(word[1:],output2)
    return sets

    
string="aab"
output=""
print(subset(string,output))