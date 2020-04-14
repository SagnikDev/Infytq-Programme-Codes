# In a fair coin we have an equal chance (50%) of either getting a ‘head’ or ‘tail’.  
# That is if we toss the coin a large number of times we would observe head approximately 50% of the time.
#  Write a program to implement a biased coin toss where the chance of getting a head is 70% (and tail 30%). 
#  That is if we invoke the program 1000 times we should see the head randomly approximately 700 times.


heads_count=[]
tails_count=[]
import random
number_of_tossed=1000
heads=int(number_of_tossed*70/100)
tails=int(number_of_tossed*30/100)
for i in range(number_of_tossed):
    if(heads>0 and tails>0):
        a=random.randrange(0,2)
        if(a==0):
            heads_count.append(0)
            heads-=1
            print("Its Heads")
        else:
            tails_count.append(1)
            tails-=1
            print("Its Tails")
    elif(tails==0):
        heads_count.append(0)
        heads-=1
        print("Its Heads")
    elif(heads==0):
        tails_count.append(1)
        tails-=1
        print("Its Tails")

print( " Number of total heads we get: {}".format(len(heads_count)))
print( " Number of total tails we get:{}".format(len(tails_count)))