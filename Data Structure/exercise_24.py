#DSA-Exer-24

def make_change(denomination_list, amount):
    changes=[]
    while(amount>0):
        denomination_list.sort(reverse=True)
        for i in denomination_list:
            if(i<=amount):
                changes.append(i)
                amount-=i
                break
    print(changes)
            

#Pass different values to the function and test your program
amount= 57
denomination_list = [1,15,10]
make_change(denomination_list, amount)