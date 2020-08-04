def toh(n,source,destination,helper):
    if(n==1):
        print("{} plate from {} to {}".format(n,source,destination))
    else:
        toh(n-1,source,helper,destination)
        print("{} plate from {} to {}".format(n,source,destination))
        toh(n-1,helper,destination,source)




source=1
destination=3
helper=2
toh(4,1,3,2)