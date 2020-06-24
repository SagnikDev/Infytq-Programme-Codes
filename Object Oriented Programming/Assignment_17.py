class Freight:
    __counter=198
    def __init__(self,recpCustmer,from_customr,weight,distance):
        self.__freight_id=None
        self.__reciptent_customer=recpCustmer
        self.__from_customer=from_customr
        self.__weight=weight
        self.__distance=distance
        self.__freight_charge=None
        Freight.__counter+=1
    def get_freight_id(self):
        return self.__freight_id
    def get_reciptent_customer(self):
        return self.__reciptent_customer
    def get_from_customer(self):
        return self.__from_customer
    def get_weight(self):
        return self.__weight
    def get_distance(self):
        return self.__distance
    def get_freight_charge(self):
        return self.__freight_charge
    def validate_weight(self):
        if(self.__weight%5==0):
            return True
        else:
                False
    def validate_distance(self):
        if(self.__distance>=500 and self.__distance<=5000):
            return True
        else:
                False
    def forward_cargo(self):
        if(self.__from_customer.validate_customer_id() and self.__reciptent_customer.validate_customer_id() and self.validate_distance() and self.validate_weight()):
            self.__freight_id=Freight.__counter+2
            self.__freight_charge=(self.__weight*150)+(self.__distance*60)
        else:
            return 0


class Customer:
    def __init__(self,cid,cname,addr):
        self.__customer_id=cid
        self.__customer_name=cname
        self.__address=addr

    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_address(self):
        return self.__address
    def validate_customer_id(self):
        if(len(str(self.__customer_id))==6 and str(self.__customer_id)[0]=="1"):
            return True
        else:
            return False
cust1=Customer(101113,"Sagnik","London")
cust2=Customer(102345,"Joy","Parris")

freight1=Freight(cust1,cust2,50,1000)