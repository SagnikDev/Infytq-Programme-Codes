vector=[]
def all_bal_paran(output,open,close):
    if(open==0 and close==0):
        print(output)
        vector.append(output)
    elif(open==0 and close>0):
        output=output+")"
        all_bal_paran(output,open,close-1)
    elif(close>open):
        output1=output+")"
        output2=output+"("
        all_bal_paran(output1,open-1,close)
        all_bal_paran(output2,open,close-1)
    else:
        output=output+"("
        all_bal_paran(output,open-1,close)
    return vector

n=3
open=n
close=n
output="("
print(all_bal_paran(output,open-1,close))