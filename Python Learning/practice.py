# import random
# import math
# # import String
# print(random.randrange(1,10))


# a=7.23
# b=6
# c=-7.23
# name='Raghav'

# print(math.ceil(a))
# print(math.floor(a))
# print(math.factorial(b))
# print(math.fabs(a))


# print(name.count('a'))
# print(name.replace('a','A'))
# print(name.find('a'))
# print(name.startswith('R'))
# print(name.endswith('av'))
# print(name.isdigit())
# print(name.upper())
# print(name.lower())
# print(name.split('a'))

# boarding_call="Good Evening, this is the final call to AI passengers for the flight AI 466 which is planned to take off at 8.40A.M."

# if(boarding_call.startswith('Good Evening')):
#     print(boarding_call.replace('Good Evening','Good Morning'))

# if(boarding_call.count('AI')>0):
#     print('Air India')
# print(boarding_call.endswith('A.M'))

# a=boarding_call.split(" ")

# for i in a:
#     if(i.isdigit()):
#         print(i)

# print(a)

# print(boarding_call.upper())

#PF-Exer-35

# def count_names(name_list):
#     count1=0
#     count2=0
#     for i in name_list:
#         if(i.endswith('at')):
#             count1+=1
#         if(i.find('at')>=0):
#             print(i)
#             count2+=1
#     #start writing your code here
#     #Populate the variables: count1 and count2

#     # Use the below given print statements to display the output
#     # Also, do not modify them for verification to work
#     print("_at -> ",count1)
#     print("%at% -> ",count2)


# #Provide different names in the list and test your program
# name_list=["at","dats"]
# count_names(name_list)

# myArray=[10,20,30,40,50,60]
# myArray.append(70)
# print(myArray)
# print(myArray.index(10))
# myArray.insert(2,23)
# print(myArray)
# myArray.pop(-2)
# print(myArray)
# myArray.remove(10)
# print(myArray)
# myArray.reverse()
# print(myArray)
# myArray.sort()
# print(myArray)


# crew_details={
#     "Pilot":"Kumar",
#     "Co-pilot":"Raghav",
#     "Head-Strewardess":"Malini",
#     "Stewardess":"Mala"
# }



# print(crew_details.get("Pilot"))

# crew_details.update({'Pilot':"Sagnik",'Attendent':'Joy'})

# print(crew_details['Pilot'])
# print(crew_details.get('Attendent'))

# import time
# import datetime
# print(time.gmtime())
# print(time.localtime())
# print(time.strftime("%d/%m/%y"))
# print(datetime.date.today().strftime("%d-%m-%y"))
# print(datetime.datetime.today())
# print(datetime.datetime.strptime("10/04/19","%d/%m/%y"))

# file_write=open('a.txt','w')
# file_write.write('Hello')
# file_write.close()

# try:
#     file=open("a.txt",'r')
#     print(file.read())
#     file.write(',Good Morning')
# except:
#     print("Error Occur")
#     if file.closed:
#         print("File is closed")
#     else:
#         print("FILE IS OPEN")
# finally:
#     print("File is being closed")
#     file.close()
#     if file.closed:
#         print("File is closed")
#     else:
#         print("FILE IS OPEN")



# try:
#     hello_file=open("flight.txt","w")
#     text="Hello everyone! Welcome"
#     hello_file.write(text)
# except:
#     print("Error occurred, not able to write to file")
# finally:
#     hello_file.close()
#     if(hello_file.closed):
#         print("File Closed")
#     else:
#         print("File not closed")
# try:
#     hello_file=open("flight.txt","r")
#     text_from_file=hello_file.read()
#     print(text_from_file)
# except:
#     print("Error Occurred, not able to read from file")
# finally:
#     hello_file.close()