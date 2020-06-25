#OOPR-Assgn-22
class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[0,0]
    __list_ticket_price=[150,200]
    mv1_counter=0
    mv2_counter=0
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        if(movie_name not in Multiplex.__list_movie_name):
            return 0
        elif(self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)==False):
            return -1
        else:
            index=Multiplex.__list_movie_name.index(movie_name)
            self.__seat_numbers=self.generate_seat_number(index,number_of_tickets)
            self.calculate_ticket_price(index,number_of_tickets)

    def  generate_seat_number(self,movie_index, number_of_tickets):
        ticket_list=[]
        for i in range(number_of_tickets):
            if(Multiplex.__list_movie_name[movie_index][-1]=="1"):
                Multiplex.mv1_counter+=1
                ticket=Multiplex.__list_movie_name[movie_index][0].upper()+Multiplex.__list_movie_name[movie_index][-1]+"-"+str(Multiplex.mv1_counter)
            else:
                Multiplex.mv2_counter+=1
                ticket=Multiplex.__list_movie_name[movie_index][0].upper()+Multiplex.__list_movie_name[movie_index][-1]+"-"+str(Multiplex.mv2_counter)
            ticket_list.append(ticket)
        Multiplex.__list_total_tickets[movie_index]-=number_of_tickets
        Multiplex.__list_last_seat_number[movie_index]+=number_of_tickets
        return ticket_list

booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())