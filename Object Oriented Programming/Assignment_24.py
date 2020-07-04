class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__price=price
        self.__item_type=item_type
        Apparel.counter+=1
        self.__item_id=item_type[0].upper()+str(Apparel.counter)
    def calculate_price(self):
        price=self.__price+(self.__price*5)/100
        self.set_price(price)
    def get_item_id(self):
        return self.__item_id
    def get_price(self):
        return self.__price
    def get_item_type(self):
        return self.__item_type
    def set_price(self,price):
        self.__price=price

class Cotton(Apparel):
    __discount=None
    def __init__(self,price,discount):
        Cotton.__discount=discount
        super().__init__(price,"Cotton")
    def calculate_price(self):
        super().calculate_price()
        price=super().get_price()
        price-=Cotton.__discount
        price+=(price*5)/100
        super().set_price(price)
    def get_discount(self):
        return Cotton.__discount

class Silk(Apparel):
    __points=None
    def __init__(self,price):
        super().__init__(price,"Silk")
        Silk.__points=( 10 if (price>10000) else 3 )
    def calculate_price(self):
        super().calculate_price()
        price=super().get_price()
        price+=(price*10)/100
        super().set_price(price)
    def get_points(self):
        return Silk.__points

c1=Cotton(100,20)
s1=Silk(10001)

c1.calculate_price()
s1.calculate_price()

print(c1.get_price())
print(c1.get_item_id())
print(c1.get_discount())


print(s1.get_price())
print(s1.get_item_id())
print(s1.get_points())