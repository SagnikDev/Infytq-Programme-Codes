import sys
class Student():
    def __init__(self,id,marks,age):
        self.__student_id=id
        self.__student_marks=(marks if marks in range(0,101) else None)
        self.__student_age=(age if age>20 else None )
        if(self.__student_marks==None or self.__student_age==None):
            print("Not Qualifying for Exam")
            sys.exit()
        else:
            print("Qualified for Exam")
    def check_qualification(self):
        if(self.__student_marks>=65):
            print("{} qualified for admission".format(self.__student_id))

stu1=Student(101,65,21)
stu1.check_qualification()