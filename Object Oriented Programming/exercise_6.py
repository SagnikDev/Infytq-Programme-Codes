#OOPR-Exer-6
#Start writing your code here
class Vehicle():
    def __init__(self,fuel,mileage):
        self.__fuel_left=fuel
        self.__mileage=mileage
    def identify_distance_that_can_be_travelled(self):
        if(self.__fuel_left<=5):
            return 0
        else:
            return self.__mileage*(self.__fuel_left-5)
    def identify_distance_travelled(self,initial_fuel):
        return (initial_fuel-self.__fuel_left)*self.__mileage
    
car=Vehicle(8,35)
print(car.identify_distance_that_can_be_travelled())
print(car.identify_distance_travelled(12))