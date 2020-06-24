class Ticket:
    counter=0
    def __init__(self,p_name,source,destination):
        self.__passenger_name=p_name
        self.__ticket_id=None
        self.__source=source
        self.__destination=destination
    def validate_source_destination(self):
        if(self.__source.lower()=="delhi" and self.__destination.lower() in ["mumbai","chennai","pune","kolkata"]):
            return True
        else:
            return False
    def generate_ticket(self):
        if(self.validate_source_destination()):
            Ticket.counter+=1
            self.__ticket_id=self.__source[0].upper()+self.__destination[0].upper()+str(Ticket.counter).zfill(2)
    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination

ticket1=Ticket("Sagnik","DeLhI","KolKaTa")
ticket1.generate_ticket()
print(ticket1.get_ticket_id())
print(ticket1.get_passenger_name())
print(ticket1.get_source())
print(ticket1.get_destination())