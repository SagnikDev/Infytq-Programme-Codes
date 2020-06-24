# Assignment 3:
# Implement the Customer class based on the identified class structure and details given below:

#     1. Consider all instance variables and methods to be public
#     2. Assume that bill_amount is initialized with total bill amount of the customer
#     3. Customer is eligible for 5% discount on the bill amount
#     4. purchases(): Compute discounted bill amount and pay bill
#     5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>

# Represent few customers, invoke purchases() method and display the details.

class Customer():
    def __init__(self,name):
        self.ammount=0
        self.name=name
        self.discount=0
    def purchases(self,amount):
        self.ammount=amount
        self.discount=self.ammount-((self.ammount*5)/100)
    def pays_bill(self,amount):
        self.purchases(amount)
        print("{} pays bill amount of Rs. {}".format(self.name,self.discount))

cust1=Customer("Sagnik")
cust1.pays_bill(1000)