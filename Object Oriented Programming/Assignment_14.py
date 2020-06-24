#OOPR-Assgn-15
#Start writing your code here
class Parrot:
    __counter=7000
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        Parrot.__counter+=1
        self.__unique_number=Parrot.__counter
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_unique_number(self):
        return self.__unique_number
    def display_parrot(self):
        print("Name= {}".format(self.get_name()))
        print("Color= {}".format(self.get_color()))
        print("Unique Number = {}".format(self.get_unique_number()))

p1=Parrot("Mithu","green")
p1.display_parrot()
p2=Parrot("Tina","Green Yellow")
p2.display_parrot()