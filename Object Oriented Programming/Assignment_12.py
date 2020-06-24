class Bill:
    def __init__(self,bill,name):
        self.bill_id=bill
        self.patient_name=name
        self.bill_amount=0
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        for i in range(0,len(quantity_list)):
            self.bill_amount+=quantity_list[i]*price_list[i]
        self.bill_amount+=consultation_fees
        print("{} of Bill Id: {} having Bill Ammount: {}".format(self.patient_name,self.bill_id,self.bill_amount))

bill1=Bill(100,"John Doe")
quantity=[2,3,5]
price=[11,33,55]
bill1.calculate_bill_amount(200,quantity,price)