class InvalidMechanicIdException(Exception):
    pass
class InvalidMechanicSpecializationException(Exception):
    pass
class Mechanic:
    def __init__(self,mechanic_id,specialization,vehicle_count):
        self.__mechanic_id=mechanic_id
        self.__specialization=specialization
        self.__vehicle_count=vehicle_count
    def get_mechanic_id(self):
        return self.__mechanic_id
    def get_specialization(self):
        return self.__specialization
    def get_vehicle_count(self):
        return self.__vehicle_count
    def set_mechanic_id(self,mechanic_id):
        self.__mechanic_id=mechanic_id
    def set_specialization(self,specialization):
        self.__specialization=specialization
    def set_vehicle_count(self,vehicle_count):
        self.__vehicle_count=vehicle_count

class VehicleService:
    def __init__(self,mechanic_list):
        self.__mechanic_list=mechanic_list
    def assign_vehicle_for_service(self,mechanic_id,vehicle_type):
        if mechanic_id not in self.__mechanic_list:
            raise InvalidMechanicIdException()
        if(self.__mechanic_list[mechanic_id].get_specialization()!=vehicle_type):
            raise InvalidMechanicSpecializationException(vehicle_type)
        self.__mechanic_list[mechanic_id].set_vehicle_count(self.__mechanic_list[mechanic_id].get_vehicle_count()+1)

m1=Mechanic(101,"TW",1)
m2=Mechanic(102,"FW",0)
m3=Mechanic(103,"TW",4)
m4=Mechanic(104,"FW",2)
m5=Mechanic(105,"FW",1)

service=VehicleService({m1.get_mechanic_id():m1,m2.get_mechanic_id():m2,m3.get_mechanic_id():m3,m4.get_mechanic_id():m4,m5.get_mechanic_id():m4})
try:
    service.assign_vehicle_for_service(101,"TW")
except InvalidMechanicIdException:
    print("This Mechanic is not in Srevice Centre")
except InvalidMechanicSpecializationException as e:
    print("This Mechanic is not Specialized for "+str(e))
