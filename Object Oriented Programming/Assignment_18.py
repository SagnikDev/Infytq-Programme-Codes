class Customer:
    def __init__(self,name):
        self.__customer_name=name
        self.__payment_status=None
    def pays_bill(self,bill):
        self.__payment_status="Paid"
        print("{} of Bill Id: {} pays Rs: {}".format(self.__customer_name,bill.get_bill_id(),bill.get_bill_amount()))
    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=None
    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
    def generate_bill_amount(item_quantity,items):
        Bill.counter+=1
        self.__bill_id="B"+str(Bill.counter)
        for i,j in item_quantity.items():
            index=items.index(i)
            price=items[index].get_price()
            self.__bill_amount+=(j*price)
class Item:
    def __init__(self,id,description,price):
        self.__item_id=id
        self.__description=description
        self.__price_per_quantity=price
    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price(self):
        return self.__price_per_quantity

