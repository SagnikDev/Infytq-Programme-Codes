#PF-Assgn-29
def calculate(distance,no_of_passengers):
    total_funds_from_pessanger=no_of_passengers*80
    fuel_price=70
    total_running_cost=(70/10)*distance
    profit=total_funds_from_pessanger-total_running_cost
    if(profit<0):
        return -1
    else:
        return profit
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))