
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue Full")
            return
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
        #Remove pass and write the logic to enqueue an element. Enqueue should be done only if queue is not full. Otherwise display appropriate message.
    def is_empty(self):
        if(self.__front==self.__rear+1):
            return True
        #Remove pass and write the logic to check whether queue is empty. If the queue is empty, return true else return false.
    
    def dequeue(self):
        if(self.__front==0 and self.__rear==0):
            data=self.__elements[self.__front]
            self.__rear=-1
            return data
        elif(self.is_empty()):
            print("Queue Empty")
            return
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        # if(self.__rear>-1 or self.__front>-1):
        for i in range(self.__front,self.__rear+1):
            print(self.__elements[i])
        #Remove pass and write the logic to display all the queue element(s).
                                                  
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg



queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Dick")
queue1.enqueue("Harry")
queue1.enqueue("Jack")
queue1.enqueue("Maria")
# queue1.enqueue("Kia")
data=queue1.dequeue()
data=queue1.dequeue()
data=queue1.dequeue()
data=queue1.dequeue()
data=queue1.dequeue()
data=queue1.dequeue()

print(data)

#Display all the elements in the queue.
# queue1.display()
                                              