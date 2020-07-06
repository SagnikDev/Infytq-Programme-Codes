from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_package_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_package_name=base_package_name
        self.__subscription_period=subscription_period
    def get_base_package_name(self):
        return self.__base_package_name
    def get_subscription_period(self):
        return self.__subscription_period
    def validate_base_pack_name(self):
        packs=["silver","gold","platinum"]
        if(self.get_base_package_name().lower() not in packs):
            self.__base_package_name="Silver"
            print("Base package name is incorrect, set to Silver")
        return True
    def calculate_monthly_rent(self):
        if(self.get_subscription_period() in range (1,25)):
            self.validate_base_pack_name()
            packs=["silver","gold","platinum"]
            monthly_rent=[350,440,560]
            index=packs.index(self.get_base_package_name().lower())
            rent=monthly_rent[index]
            if(self.get_subscription_period()>12):
                discount=rent
            final_monthly_rent=((rent*self.__subscription_period)-rent)/self.__subscription_period
            return final_monthly_rent
        else:
            return -1

pack1=BasePackage("Sagnik","Gold",24)
print(pack1.calculate_monthly_rent())