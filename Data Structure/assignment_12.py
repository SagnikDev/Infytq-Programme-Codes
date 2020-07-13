#DSA-Assgn-12
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        if(self.is_full()):
            print("Stack Full")
            return
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    
        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        else:
            return False
        #Remove pass and write the logic to check whether stack is empty. If the stack is empty, return true else return false.
    
    def pop(self):
        if(self.is_empty()):
            print("Stack Empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            # return self.__elements[self.__top+1]
            return data
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message

    def display(self):
        for i in range(0,self.__top+1):
            print(self.__elements[i])                                      
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

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

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        
    def __str__(self):
        return (self.__color+" "+self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
     
#Implement Game class here
class Game:
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=Stack(2)
        self.green_balls_container=Stack(2)
        self.blue_balls_container=Stack(2)
        self.yellow_balls_container=Stack(2)
    def grouping_based_on_color(self):
        while(self.ball_container.is_empty()==False):
            ball=self.ball_container.pop()
            if(ball.get_color()=="Red"):
                self.red_balls_container.push(ball)
            elif(ball.get_color()=="Blue"):
                self.blue_balls_container.push(ball)
            elif(ball.get_color()=="Green"):
                self.green_balls_container.push(ball)
            else:
                self.yellow_balls_container.push(ball)
    def display_ball_details(self,color):
        if(color=="Red"):
            print(self.red_balls_container)
        elif(color=="Blue"):
            print(self.blue_balls_container)
        elif(color=="Green"):
            print(self.green_balls_container)
        else:
            print(self.yellow_balls_container)
    def rearrange_balls(self,color):
        if(color=="Red"):
            red_balls_container=self.arrange(self.red_balls_container)
        elif(color=="Blue"):
            blue_balls_container=self.arrange(self.blue_balls_container)
        elif(color=="Green"):
            green_balls_container=self.arrange(self.green_balls_container)
        else:
            yellow_balls_container=self.arrange(self.yellow_balls_container)
    def arrange(self,contaier):
        data=contaier.pop()
        if(data.get_name()=="B"):
            arr=[]
            arr.append(data)
            arr.append(contaier.pop())
            contaier.push(arr[0])
            contaier.push(arr[1])
            return contaier
        else:
            contaier.push(data)
            return contaier

#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

#Create objects of Game class, invoke the methods and test the program
game1=Game(ball_list)
game1.grouping_based_on_color()

game1.display_ball_details("Red")
game1.rearrange_balls("Red")
game1.display_ball_details("Red")
