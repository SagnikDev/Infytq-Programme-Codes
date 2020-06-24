import sys
class Vehicle():
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    def setter(self,id,vtype,cost):
        self.__vehicle_id=id
        self.__vehicle_type=str.lower(vtype).replace(" ","")
        self.__vehicle_cost=cost
    def calculate_premium(self):
        if(self.__vehicle_type=="twowheeler"):
            self.__premium_amount=(self.__vehicle_cost*2)/100
        elif(self.__vehicle_type=="fourwheeler"):
           self.__premium_amount=(self.__vehicle_cost*6)/100 
        else:
            print("Unknown Vehicle")
            sys.exit()
    def display_vehicle_details(self):
        print("Your Vehicle \" {} \" have premium of Rs: {}".format(self.__vehicle_id,self.__premium_amount))
        
v1=Vehicle()
v1.setter("WB 12AH 2604","tWO Wheeler",70000)
v1.calculate_premium()
v1.display_vehicle_details()