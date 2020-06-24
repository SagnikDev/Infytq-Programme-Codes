#OOPR-Assgn-10

class CallDetail:
    def __init__(self,phno,called,durtn,ctype):
        self.phoneno=phno
        self.called_no=called
        self.duration=durtn
        self.call_type=ctype

class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for calls in list_of_call_string:
            call_data=calls.split(",")
            a=call_data[0]
            b=call_data[1]
            c=call_data[2]
            d=call_data[3]
            self.list_of_call_objects.append(CallDetail(a,b,c,d))

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)