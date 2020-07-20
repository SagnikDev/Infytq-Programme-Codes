#DSA-Exer-22

def order_heights(student_list,height_list):
    #Write your logic here
    students={}
    for i in range(0,len(student_list)):
        students[height_list[i]]=student_list[i]
    
    students=sorted(students.items())
    student_list=[]
    height_list=[]
    for i in range(0,len(students)):
        height_list.append(students[i][0])
        student_list.append(students[i][1])
    return[student_list,height_list]


#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])