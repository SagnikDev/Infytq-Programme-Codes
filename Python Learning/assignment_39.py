#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    index=[]
    quantity_requested=[]
    for i in range(1,len(item_tuple)+1):
        if(int(i%2)==0):
            quantity_requested.append(item_tuple[i-1])
        else:
            index.append(item_tuple[i-1])
    for i in range(0,len(index)):
        check=check_quantity_available(index[i],quantity_requested[i])
        if(check==True):
            print("{} is available".format(index[i]))
        elif(check==False):
            print("{} stock is over".format(index[i]))
        elif(check==-1):
            print("{} is not available".format(index[i]))


    #Remove pass and write your logic here


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(index in menu):
        index_menu=menu.index(index)
        quantity=quantity_available[index_menu]
        if(quantity>=quantity_requested):
            quantity_available[index_menu]-=quantity
            return True
        else:
            return False
    else:
        return -1

    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)