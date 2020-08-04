def perm_wth_case_chng(output,input):
    if(len(input)==0):
        print(output)
    else:
        output1=output+input[0].upper()
        output2=output+input[0]
        input=input[1:]
        perm_wth_case_chng(output1,input)
        perm_wth_case_chng(output2,input)

input="ab"
output=""
perm_wth_case_chng(output,input)