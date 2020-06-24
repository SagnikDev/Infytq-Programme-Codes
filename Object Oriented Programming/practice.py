class Mobile():
    def __init__(self,price,brand):
        #Private variables
        self.__price=price
        self.__brand=brand

    def getter(self):
        print("Your {} phone cost is Rs: {}".format(self.__brand,self.__price))


mob1=Mobile(10000,"Lenovo")
mob2=Mobile(20000,"Apple")

mob1.getter()
mob2.getter()
mob1.__price=10009
mob1.getter()
#Unloacking Private variables
mob1._Mobile__price=10010
mob1.getter()