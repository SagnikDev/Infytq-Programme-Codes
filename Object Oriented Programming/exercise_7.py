#OOPR-Exer-7
#Start writing your code here
class Ticket:
    counter=00
    def __init__(self,name,source,destination):
        self.passenger_name=name
        self.ticket_id=None
        self.source=source
        self.destination=destination
        Ticket.counter+=1
        self.counter=Ticket.counter
    def validate_source_destination(self):
        if(self.source.lower()==str.lower("Delhi") and self.destination.lower() in ["mumbai","chennai","pune","kolkata"]):
            return True
        else:
            return False
    def generate_ticket(self):
        if(self.validate_source_destination()):
            counter=str(self.counter).zfill(2)
            self.ticket_id=self.source[0].upper()+self.destination[0].upper()+counter
            print(self.source[0].upper()+self.destination[0].upper()+counter)
        else:
            self.ticket_id=None

p1=Ticket("Sagnik","Delhi","Chennai")
p1.generate_ticket()
p2=Ticket("Sagnik","Delhi","Mumbai")
p2.generate_ticket()
p3=Ticket("Sagnik","Delhi","Kolkata")
p3.generate_ticket()