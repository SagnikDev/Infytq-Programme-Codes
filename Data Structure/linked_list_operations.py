#DSA-Exer-2

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    
    def display(self):
        print("The Containts of Linked List is:")
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()

    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            else:
                temp=temp.get_next()
        return None

    def insert(self,data,data_before):
        new_node=Node(data)
        data_before=self.find_node(data_before)
        if(data_before==None):
            print(" Error! Data Before Not Found")
        else:
            new_node.set_next(data_before.get_next())
            data_before.set_next(new_node)
            if(new_node.get_next()==None):
                self.__tail=new_node
    def delete(self,data):
        node=self.find_node(data)
        if(node==None):
            print("Error! Node Doesnot exist in Linked List")
        elif(self.__head==node):
            self.__head=node.get_next()
        else:
            temp=self.__head
            while(temp.get_next() is not node):
                temp=temp.get_next()
            if(temp.get_next()==self.__tail):
                temp.set_next(None)
                self.__tail=temp
            else:
                temp.set_next(node.get_next())
                node.set_next(None)

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


biscuit_list=LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")



node=biscuit_list.find_node("Goodday")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
print("-----After Inserting Marie-----")
biscuit_list.insert("Marie","Hide&Seek")
biscuit_list.display()
print("----After Deleting Marie-----")
biscuit_list.delete("Marie")
biscuit_list.display()