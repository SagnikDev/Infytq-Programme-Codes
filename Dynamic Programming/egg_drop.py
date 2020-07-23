#Egg Dropping Puzzle

def eggDrop(n,k):
    if(k==1):
        return n
    elif(n==1):
        return k
    for i in range(1,k+1):
        