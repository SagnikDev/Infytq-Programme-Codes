#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    level=[0,0,0,15,7,5]
    new_salary=current_salary+(current_salary*(level[job_level]/100))
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)