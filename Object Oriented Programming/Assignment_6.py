class Instructor:
    def __init__(self,name,skill,feedback,exp):
        self.__instructor_name=name
        self.__technology_skill=skill
        self.__avg_feedback=feedback
        self.__experience=exp

    def check_eligibility(self):
        if(self.__experience>3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False
    def allocate_course(self,technology):
        if(self.check_eligibility()):
            print("{} is appointed for {}".format(self.__instructor_name,self.__technology_skill))
        else:
            print("{} is not eligible for {}".format(self.__instructor_name,self.__technology_skill))

inst1=Instructor("Sagnik","Python",4,3)
inst1.allocate_course("Python")