#PF-Assgn-53
#This verification is based on string match.

poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.
import re
#Write your logic here for question 1
v_finder=re.compile(r'v')
poem_v=v_finder.findall(poem)
print(len(poem_v))

remove_newline=re.compile(r'\n')
poem_RV_NLN=remove_newline.sub("\1 ",poem)
print(poem_RV_NLN)

sub_ch_co=re.compile(r"c((h)|(o))")
poem_ch_co=sub_ch_co.sub(r'C\1',poem)
print(poem_ch_co)

sub_ai_hi=re.compile(r"(ai|hi)(...)")
poem_ai_hi=sub_ai_hi.sub(r"\1*\*",poem)
print(poem_ai_hi)