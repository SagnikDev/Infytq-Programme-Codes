def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def max_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1]>heap.element[i-1]):
        largest=left
    else:
        largest=i
    if(right<=heap.length and heap.element[right-1]>heap.element[largest-1]):
        largest=right
    if(largest!=i):
        swap(heap.element,i-1,largest-1)
        max_heapify(heap,largest)

def build_max_heap(heap):
    length=heap.length
    for i in range(length//2,0,-1):
        max_heapify(heap,i)

def heap_extract_max(heap):
    length=heap.length
    if(length<1):
        print("Heap Underfolw")
    else:
        max=heap.element[0]
        heap.element[0]=heap.element[length-1]
        heap.length=length-1
        max_heapify(heap,1)
        return max

def heap_sort(heap):
    sets=[]
    while(heap.length>0):
        max=heap_extract_max(heap)
        sets.append(max)
    return sets

def heap_increase_key(heap,i,key):
    if(key<heap.element[i-1]):
        print("Increase Error")
    else:
        heap.element[i-1]=key
        while(i>1 and heap.element[(i//2)-1]<heap.element[i-1]):
            swap(heap.element,i-1,(i//2)-1)

class Heap():
    def __init__(self,setter=[]):
        self.element=[]
        if(len(setter)!=0):
            for i in setter:
                self.element.append(i)
        self.length=len(self.element)

        

# heap=[1,14,10,8,7,9,3,2,4,6]
# # i=1
# # max_heapify(heap,i)
# build_max_heap(heap)

# print(heap)

heap=Heap([1,5,6,8,12,14,16])
i=1
max_heapify(heap,1)
# build_max_heap(heap)
print(heap.element)
# heap_increase_key(heap,3,18)
# print(heap.element)
# build_max_heap(heap)
# print(heap_extract_max(heap))
# print(heap.element)
# sets=heap_sort(heap)
# print(sets)
