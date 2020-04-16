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

import time
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


# Regular Expression
import re
# string="Airline"
# if(re.search(r"\*","Air*line")):
#     print("Found * escape sequence")
# if(re.search(r"A..l","Airline")):
#     print("Found Airline")
# if(re.search(r"A\d*","A2irline")):
#     print("Found Airline")
# if(re.search(r"A[2-4]*l","A2irline")):
#     print("Found Airline")
# if(re.search(r"Air | Chair","A2irline")):
#     print("Found Airline")
# if(re.search(r"Air\s","Air line")):
#     print("Found Air line")
# if(re.search(r"Air\d*","Airline")):
#     print("Found Air[0-n]ine")
# if(re.search(r"Air\d+","Air123444line")):
#     print("Found Air[1-n]ine")
# if(re.search(r"Air\d?l","Air1line")):
#     print("Found Air[0 or 1 times]ine")
# if(re.search(r"Air\d{3}l","Air122line")):
#     print("Found Air[3 times number]ine")
# if(re.search(r"^A","Air1line")):
#     print("Found Starts with A")
# if(re.search(r"e$","Air1line")):
#     print("Found Ends with e")
# if not (re.search(r"\w$","Air1line@")):
#     print("Found Ends with Alphanumeric")


# flight_details="Flight Savana Airlines a2138"

# print(re.sub(r"Flight","Plane",flight_details))
# print(re.sub(r"a(\d{4})",r"A\1",flight_details))

                                          

#Regular Expression
phoneNumber=re.compile(r'(\d\d\d)-(\d\d\d)')
no=phoneNumber.search("My phone number is 112-332")
# print(no.group())
# print(no.group(0))
# print(no.group(1))
# print(no.group(2))
# print(no.groups())
# a,b=no.groups()
# print(b)
heroes=re.compile(r"Batman | Spiderman ")
a=heroes.search('I saw Batman and Spiderman both')


heroes=re.compile(r"Bat(man|can|dan)")
a=heroes.search('I saw Batman and Spiderman both')

heroes=re.compile(r"Bat(wo)?man")
a=heroes.search('I saw Batman dancing on the street')


heroes=re.compile(r"Bat(wo)?man")
a=heroes.search('I saw Batwoman dancing on the street')


phoneNumber=re.compile(r'(\d\d\d\d-)?\d-\d\d\d-\d\d\d')
mo=phoneNumber.search('My phone number is 2-530-803')

mo=phoneNumber.search('My phone number is 0341-2-530-803')

heroes=re.compile(r"Bat(wo)*man")
a=heroes.search('I saw Batman dancing on the street')

a=heroes.search('I saw Batwoman dancing on the street')

a=heroes.search('I saw Batwowoman dancing on the street')

heroes=re.compile(r'Bat(wo)+man')
a=heroes.search('I saw Batwoman dancing on the street')
# print(a.group())
a=heroes.search('I saw Batwowoman dancing on the street')


heroes=re.compile(r'(Bat){3}')
a=heroes.search('I saw a BatBatBat man')


heroes=re.compile(r'(Bat){3,7}')
a=heroes.search('I saw a BatBatBatBatBat man')



phoneNumber=re.compile(r'(\+\d\d-)?(\d\d\d\d\d)-(\d\d\d\d\d)')
mo=phoneNumber.search('My phone number is 94752-45371 also i have a phone number of +91-70014-16691')
# print(mo.group())
#Findall Method
phoneNumber=re.compile(r'(\+\d\d-)?(\d\d\d\d\d-\d\d\d\d\d)')
mo=phoneNumber.findall('My phone number is 94752-45371 also i have a phone number of +91-70014-16691')
# print(mo.group())
# print(mo)

xmRegx=re.compile(r"\d{2}\s\w+")
mo=xmRegx.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo)

vowelRegx=re.compile(r"[aeiouAEIOU]")
mo=vowelRegx.findall("Sagnik Roy")
# print(mo)

consonantRegx=re.compile(r"[^aeiouAEIOU]")
mo=consonantRegx.findall("Sagnik Roy")
# print(mo)

beginRegx=re.compile(r"^Hello")
endwithRegx=re.compile(r"\d$")

mo=beginRegx.search("Hello World the time is now 2:03")
# print(mo.group())
mo=endwithRegx.search("Hello World the time is now 2:03")
# print(mo.group())

numberRegx=re.compile(r"^\d+$")
mo=numberRegx.search("9475245371")


wildcartRegx=re.compile(r".at")
mo=wildcartRegx.search("The cat is running")
# print(mo.group())

#.*
nongreedyRegex=re.compile(r"<.*?>")
mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())
greedyRegex=re.compile(r"<.*>")
mo =greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

nonewLine=re.compile(r".*")
mo=nonewLine.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())
withnewLine=re.compile(r".*",re.DOTALL)
mo=withnewLine.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
# print(mo.group())

robocop=re.compile(r"robocop",re.I)
mo=robocop.search("RoboCop protects humans")
# print(mo.group())

#sub() subsitute command
nameRegx=re.compile(r'Agent \w+')
mo=nameRegx.sub('DEVELOPERS','Agent Aliace save the world')
# print(mo)

nameRegx=re.compile(r'Agent (\w)\w*')
# mo=nameRegx.sub('DEVELOPERS','Agent Aliace save the world')
mo=nameRegx.sub(r"Agent \1****","Agent Aliace save the world from Agent Bob who is ordered by Agent Robby")
# print(mo.group())
# print(mo)



flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"


#This function returns the values in the search result
# def printout(search_result):
#     if(search_result!=None):
#         return search_result.group()
#     else:
#         return "No Output"


# b_ays=re.compile(r"B\w+\sA\w+")
# search_result =b_ays.search(flight_details)
# print(printout(search_result))
# time=re.compile(r"\d\d\:\d\d")
# search_result =time.search(flight_details)
# print(printout(search_result))
# good=re.compile(r"good",re.I)
# search_result =good.search(flight_details)
# print(printout(search_result))
# flight=re.compile(r"F\w+t")
# search_result =flight.search(flight_details)
# print(printout(search_result))
# upper_case=re.compile(r"\w+(\d{4})")
# search_result =upper_case.sub(r"BA\1",flight_details)
# print(search_result)




from threading import Thread

# def try1():
#     for i in range(10):
#         print("This is from Thread1")
#     print("This is final from Thread1")
# def try2():
#     for j in range(10):
#         print("This is from Thread2")
#     print("This is final from Thread2")
# thread1=Thread(target=try1)
# thread2=Thread(target=try2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


#PF-Tryout

# def func1():
#     result_sum=0
#     #Write the code to find the sum of numbers from 1 to 10000000
#     for i in range(10000000):
#         result_sum=result_sum+i
#     print("Sum from func1:",result_sum)

# def func2():
#     result_sum=0
#     #Write the code to accept 5 numbers from user and find its sum
#     for i in range(10000000):
#         result_sum=result_sum+i
#     print("Sum from func2:",result_sum)

# #Modify the code given below to execute func1() and func2() in two separate threads
# # func1()
# # func2()
# thread1=Thread(target=func1)
# thread2=Thread(target=func2)

# thread1.start()
# thread2.start()


# thread1.join()
# thread2.join()
# import math

# g=(lambda x,y: x*(x+y) )

# print(g(7,3))

# s=(lambda x:math.factorial(x))
# print(s(7))

# h=(lambda x: x>40)
# print(h(50))

# m=(lambda x,y,z:x+y)

# print(m(1,2,3))



# principal_amount=20
# duration=10
# rate_of_interest=10

# simple_interest =(lambda p,d,r: (p*d*r)/100 )

# # if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
# #     print("Platinum Member"+str(simple_interest))
# # else:
# #     print("Gold Member"+str(simple_interest))

# print(simple_interest(principal_amount,duration,rate_of_interest))



def sum_all(function, data):
    result_sum=0
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum

Q=[1,3,4,5,6,7,8,9,10,15,20]

p = lambda x:x

q = lambda x : x%2 == 0

r = lambda x : x%3 == 0


print(sum_all(p,Q))
print(sum_all(q,Q))
print(sum_all(r,Q))