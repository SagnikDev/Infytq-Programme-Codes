def p_with_spaces(output,input):
    if(len(input)==0):
        print(output)
    else:
        output1=output+"_"+input[0]
        output2=output+input[0]
        input=input[1:]
        p_with_spaces(output1,input)
        p_with_spaces(output2,input)



permutation="abc"
output=permutation[0]
input=permutation[1:]
p_with_spaces(output,input)