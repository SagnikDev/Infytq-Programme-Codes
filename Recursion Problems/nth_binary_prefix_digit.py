def nth_binary_prefix_digits(output,ones,zeroes,n):
    if(n==0):
        print(output)
    elif(ones>zeroes):
        nth_binary_prefix_digits(output+"1",ones+1,zeroes,n-1)
        nth_binary_prefix_digits(output+"0",ones,zeroes+1,n-1)
    else:
        nth_binary_prefix_digits(output+"1",ones,zeroes+1,n-1)

n=3
zeroes=0
ones=1
output="1"
nth_binary_prefix_digits(output,ones,zeroes,n-1)