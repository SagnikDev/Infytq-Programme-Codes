from abc import ABCMeta,abstractmethod
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_amount=0
        self.bill_id=None
    @abstractmethod
    def calculate_bill_amount(self):
        pass
    def get_customer_name(self):
        return self.__customer_name
class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        OccasionalCustomer.__counter+=1
        self.bill_id="O"+str(OccasionalCustomer.__counter)
        self.__distance_in_kms=distance_in_kms
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def calculate_bill_amount(self):
        if(self.validate_distance_in_kms()):
            tiffin_cost=50
            if(self.__distance_in_kms in range(1,3)):
                delivery_charge=5*self.__distance_in_kms
            else:
                delivery_charge=7.5*self.__distance_in_kms
            self.bill_amount=tiffin_cost+delivery_charge
            return tiffin_cost+delivery_charge
        else:
            self.bill_amount=-1
            return -1
    def validate_distance_in_kms(self):
        if(self.__distance_in_kms in range(1,6)):
            return True
        else:
            return False
class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        RegularCustomer.__counter+=1
        self.bill_id="R"+str(RegularCustomer.__counter)
        self.__no_of_tiffin=no_of_tiffin
    def calculate_bill_amount(self):
        if(self.validate_no_of_tiffin()):
            tiffin_cost=50
            self.bill_amount=tiffin_cost*self.__no_of_tiffin*7
            return self.bill_amount
        else:
            self.bill_amount=-1
            return self.bill_amount
    def validate_no_of_tiffin(self):
        if(self.__no_of_tiffin in range (1,8)):
            return True
        else:
            return False
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

OC1=OccasionalCustomer("Sagnik Roy",2)
print(OC1.calculate_bill_amount())
print(OC1.bill_id)

RC1=RegularCustomer("Joy",1)
print(RC1.calculate_bill_amount())
print(RC1.bill_id)