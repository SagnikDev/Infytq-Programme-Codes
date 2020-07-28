class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.elements=[None]*self.__max_size
        self.top=-1
    
    def is_full(self):
        if(self.top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.top+=1
            self.elements[self.top]=data
    
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.elements[self.top]
            self.top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.top
            while(index>=0):
                print(self.elements[index])
                index-=1
    
    def get_max_size(self):
        return self.__max_size
                                                   
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.top
        while(index>=0):
            msg.append((str)(self.elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

def insert_stack(stack,element):
    if(stack.is_empty()==True):
        stack.push(element)
        return stack
    last=stack.pop()
    stack=insert_stack(stack,element)
    stack.push(last)
    return stack
def reverse_stack(stack):
    if(stack.is_empty()==True):
        return stack
    last=stack.pop()
    stack=reverse_stack(stack)
    stack=insert_stack(stack,last)
    return stack 

ball_stack=Stack(6)
ball_stack.push(1)
ball_stack.push(2)
ball_stack.push(3)
ball_stack.push(4)
ball_stack.push(5)
ball_stack.push(6)
print("---Before Inserting----")
ball_stack.display()
print("---After Inserting----")
stack=reverse_stack(ball_stack)
stack.display()