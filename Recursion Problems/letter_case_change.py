def letter_case_change(input,output):
    if(len(input)==0):
        print(output)
    else:
        if(input[0].isnumeric()==True):
            output=output+input[0]
            input=input[1:]
            letter_case_change(input,output)
        else:
            output1=output+input[0].upper()
            output2=output+input[0].lower()
            input=input[1:]
            letter_case_change(input,output1)
            letter_case_change(input,output2)


input="a1B2"
output=""
letter_case_change(input,output)