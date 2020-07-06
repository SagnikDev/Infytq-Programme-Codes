class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
    def validate_quantity(self):
        if(self.__quantity in range (1,6)):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
class Pizzaservice():
    counter=100
    def __init__(self,customer,pizza_type,additional_toping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_toping
        self.pizza_cost=0
        Pizzaservice.counter+=1
        self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter)
    def validate_pizza_type(self):
        if(self.__pizza_type.lower()=="small" or self.__pizza_type.lower()=="medium"):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if(self.validate_pizza_type() and self.__customer.validate_quantity()):
            if(self.__pizza_type.lower()=="small"):
                cost=150*self.__customer.get_quantity()
                if(self.__additional_topping==True):
                    cost+=(35*self.__customer.get_quantity())
            else:
                cost=200*self.__customer.get_quantity()
                if(self.__additional_topping==True):
                    cost+=(50*self.__customer.get_quantity())
            self.pizza_cost=cost
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer.get_customer_name()
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms
    def validate_distance_in_kms(self):
        if(self.__distance_in_kms in range(1,11)):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if(self.validate_distance_in_kms()):
            super().calculate_pizza_cost()
            if(self.__distance_in_kms<=5):
                self.pizza_cost+=(self.__distance_in_kms*5)
            else:
                self.pizza_cost+=(self.__distance_in_kms*7)
        else:
            self.pizza_cost=-1
    def get_delivery_charges(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms

c1=Customer("Sagnik",4)
p1=Pizzaservice(c1,"Medium",False)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
d1=Doordelivery(c1,"Medium",False,5)
d1.calculate_pizza_cost()
print(d1.pizza_cost)