# Python program to print postorder 
# traversal from preorder and 
# inorder traversals 
def printpostorder(inorder, preorder, n): 
	if preorder[0] in inorder: 
		root = inorder.index(preorder[0]) 
		
	if root != 0: # left subtree exists 
		printpostorder(inorder[:root], 
					preorder[1:root + 1], 
					len(inorder[:root])) 
	
	if root != n - 1: # right subtree exists 
		printpostorder(inorder[root + 1:], 
					preorder[root + 1:], 
					len(inorder[root + 1:])) 
	
	print (preorder[0])
		
# Driver Code 
inorder = ["D","H","B","E","A","I","F","C","J","G","K"]; 
preorder = ['A',"B",'D',"H","E",'C',"F",'I','G','J','K']; 
n = len(inorder) 
print ("Postorder traversal ")
printpostorder(inorder, preorder, n)