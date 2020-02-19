#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if((food_type=="V" or food_type=="N") and (quantity_ordered>0 and distance_in_kms>0)):
        if(distance_in_kms<=3):
            distance_in_kms=0
        elif(distance_in_kms>3 and distance_in_kms<=6):
            distance_in_kms*=3
        else:
            distance_in_kms*=6
        if(food_type=="V"):
            bill_amount=120*quantity_ordered+distance_in_kms
        else:
            bill_amount=150*quantity_ordered+distance_in_kms
    else:
        bill_amount=-1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)
