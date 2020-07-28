class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def height(root):
    if(root==None):
        return 0
    return 1 + max(height(root.left),height(root.right))


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4)
root.left.left = Node(4)
root.left.rigt = Node(4)
root.left.left.left = Node(4)
root.left.left.right = Node(4)
root.left.right = Node(5)

print("Height of that Binary tree: " )
print(height(root))