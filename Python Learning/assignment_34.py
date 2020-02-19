#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    i=1
    j=len(num_list)/2
    count=0
    while(i<=j):
        a=num_list.pop()
        print("Popped",a)
        if(a>n):
            i+=1
            print("Continued",a)
            continue
        else:
            required=n-a
            print("Required",required)
            if(required in num_list):
                print("Reuired found")
                count+=1
                num_list.remove(required)
        i+=1
    return (count)

num_list=[1,2,3,4,5,6]
n=10
print(find_pairs_of_numbers(num_list,n))