import heapq

li=[1,5,6,8,12,14,16]

# print ("The created heap is : ",end="") 
# print (list(li))

heapq.heappush(li,4) 

# print ("The modified heap after push is : ",end="") 
# print (list(li))

# print ("The popped and smallest element is : ",end="") 
# print (heapq.heappop(li))
# print (list(li))

# initializing list 1 
li1 = [5, 7, 9, 4, 3] 
  
# initializing list 2 
li2 = [5, 7, 9, 4, 3] 

# using heapify() to convert list into heap 
# heapq.heapify(li1) 
# heapq.heapify(li2) 

heapq.heappush(li1,8)

# heapq.heapify(li1) 

print(li1)