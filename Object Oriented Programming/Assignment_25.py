class FruitInfo:
    __fruit_name_list=["apple","guava","orange","grape","sweetlime"]
    __fruit_price_list=[200,80,70,110,60]
    @staticmethod
    def get_fruit_price(fruit_name):
        if(fruit_name.lower().replace(" ","") in FruitInfo.__fruit_name_list):
            index=FruitInfo.__fruit_name_list.index(fruit_name.lower().replace(" ",""))
            return FruitInfo.__fruit_price_list[index]
        else:
            return -1
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

class Customer():
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__customer_type=cust_type
    def get_customer_name(self):
        return self.__customer_name
    def get_customer_type(self):
        return self.__customer_type

class Purchase:
    __counter=100
    def __init__(self,customer,fruit_name,quantity):
        self.customer=customer
        self.fruit_name=fruit_name
        self.quantity=quantity
        Purchase.__counter+=1
        self.purchase_id="P"+str(Purchase.__counter)
    def get_customer(self):
        return self.customer.get_customer_type()
    def get_puchase_id(self):
        return self.purchase_id
    def get_quantity(self):
        return self.quantity
    def calculate_price(self):
        price=FruitInfo.get_fruit_price(self.fruit_name)
        if(price!=-1):
            price*=self.quantity
            max_fruit_price=max(FruitInfo.get_fruit_price_list())
            min_fruit_price=min(FruitInfo.get_fruit_price_list())
            if(FruitInfo.get_fruit_price(self.fruit_name)==max_fruit_price and self.quantity>1):
                price-=(price*2)/100
            elif(FruitInfo.get_fruit_price(self.fruit_name)==min_fruit_price and self.quantity>=5):
                price-=(price*5)/100
            if(self.get_customer().lower()=="wholesale"):
                price-=(price*10)/100
            return price
        else:
            return -1
c1=Customer("Sagnik","wholesale")
p1=Purchase(c1,"orange",10)
print(p1.calculate_price())