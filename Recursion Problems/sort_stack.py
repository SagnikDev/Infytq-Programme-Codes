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

def sort_stack(ball_stack):
    if(ball_stack.is_empty()==True):
        return ball_stack
    last=ball_stack.pop()
    stack=sort_stack(ball_stack)
    stack=put_stack(ball_stack,last)
    return stack


def put_stack(stack,temp):
    if(stack.is_empty()==True or stack.elements[stack.top]<temp):
        stack.push(temp)
        return stack
    last=stack.pop()
    stack=put_stack(stack,temp)
    stack.push(last)
    return stack



ball_stack=Stack(7)
ball_stack.push(2)
ball_stack.push(3)
ball_stack.push(7)
ball_stack.push(6)
ball_stack.push(4)
ball_stack.push(5)
ball_stack.push(9)
print("-----Before Sorting-------")
ball_stack.display()
print()
print("-----After Sorting-------")
stack=sort_stack(ball_stack)
stack.display()

