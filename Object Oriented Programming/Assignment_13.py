class Classroom:
    __classroom_list=[]
    @staticmethod
    def search_classroom(class_room):
        if(class_room.lower() in Classroom.__classroom_list):
            return "Found"
        else:
            return -1
    @staticmethod
    def add_Room(room):
        Classroom.__classroom_list.append(room.lower())

Classroom.add_Room("Room1")
Classroom.add_Room("Room2")
Classroom.add_Room("Room2")
print(Classroom.search_classroom("Room2"))