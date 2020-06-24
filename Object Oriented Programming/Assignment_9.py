import sys
class Student():
    def __init__(self,id,marks,age):
        self.__student_id=id
        self.__student_marks=(marks if marks in range(0,101) else None)
        self.__student_age=(age if age>20 else None )
        self.__course_id=[x for x in range(100,111)]
        self.__fees=1000
        if(self.__student_marks==None or self.__student_age==None):
            print("Not Qualifying for Exam")
            sys.exit()
        else:
            print("Qualified for Exam")
    def check_qualification(self):
        if(self.__student_marks>=65):
            print("{} qualified for admission".format(self.__student_id))
        else:
            print("Not Qualifying for Admission")
            sys.exit()
    def choose_course(self,course_id):
        if(course_id in self.__course_id):
            if(self.__student_marks>85):
                print("Cource {} is available and its prices Rs: {}".format(course_id,self.__fees-((self.__fees*25)/100)))
            else:
                print("Cource {} is available and its prices Rs: {}".format(course_id,self.__fees))
        else:
            print("Course is not available")




stu1=Student(101,88,21)
stu1.check_qualification()
stu1.choose_course(111)