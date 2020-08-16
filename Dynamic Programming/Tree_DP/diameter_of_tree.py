import sys
def solve(root,res):
    if(root==None):
        return 0,0
    left,reslt=solve(root.left,res)
    right,reslt=solve(root.right,res)

    temp=1+max(left,right)
    ans=max(temp,left+right+1)
    res=max(res,ans)

    return temp,res




class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        print(self.data)

root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(6)
root.left.right.right=Node(7)
root.right.right=Node(8)
root.right.right.right=Node(9)
root.right.right.right.left=Node(10)
root.right.right.right.right=Node(11)
root.right.right.right.left.left=Node(12)
root.right.right.right.left.right=Node(13)

#Code
res=-1
temp,res=solve(root,res)
print(res)