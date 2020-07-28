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

def delete_m(stack,mid):
    if(stack.is_empty()==True):
        return stack
    if(mid==1):
        stack.pop()
        return stack
    last=stack.pop()
    stack=delete_m(stack,mid-1)
    stack.push(last)
    return stack


ball_stack=Stack(6)
ball_stack.push(1)
ball_stack.push(2)
ball_stack.push(3)
ball_stack.push(4)
ball_stack.push(5)
ball_stack.push(6)


stack=delete_m(ball_stack,(ball_stack.get_max_size()//2)+1)
stack.display()