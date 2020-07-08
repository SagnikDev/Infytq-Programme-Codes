#DSA-Assgn-2

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service:
    def __init__(self,car_list):
        self.__car_list=car_list
    def get_car_list(self):
        return self.__car_list
    def find_cars_by_year(self,year):
        cars=[]
        for car in self.__car_list:
            if(car.get_year()==year):
                cars.append(car.get_model())
        if(len(cars)>=1):
            return cars
        else:
            return None
    def add_cars(self,new_car_list):
        car_list_new={}
        car_list=[]
        for car in new_car_list:
            car_list_new[car.get_year()]=car
        car_list_new_sorted=sorted(car_list_new.items())
        for i in car_list_new_sorted:
            car_list.append(i[1])
        self.__car_list=car_list
    def remove_cars_from_karnataka(self):
        for car in self.__car_list:
            if(car.get_registration_number().startswith("KA")):
                self.__car_list.remove(car)

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program
service1=Service(car_list)
print(service1.find_cars_by_year(2013))
car6=Car("Bajaj",2012,"WB12AH 2604")
car_list=[car1, car2, car3, car4,car5,car6]
service1.add_cars(car_list)
service1.remove_cars_from_karnataka()