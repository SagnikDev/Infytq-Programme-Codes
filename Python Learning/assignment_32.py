#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    sum=0
    collection={}
    for i in medical_speciality:
        for j in range(0,len(patient_medical_speciality_list)):
            if(patient_medical_speciality_list[j]==i):
                sum=sum+patient_medical_speciality_list[j-1]
        collection[sum]=i
        sum=0
    # return speciality
    return medical_speciality[collection[max(collection)]]

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)