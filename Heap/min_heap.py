def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def min_heapify(heap,i):
    left=2*i
    right=2*i+1

    if(left<=heap.length and heap.element[left-1]<heap.element[i-1]):
        smallest=left
    else:
        smallest=i
    if(right<=heap.length and heap.element[right-1]<heap.element[smallest-1]):
        smallest=right
    if(smallest!=i):
        swap(heap.element,i-1,smallest-1)
        min_heapify(heap,smallest)

def build_min_heap(heap):
    length=heap.length
    for i in range(length,0,-1):
        min_heapify(heap,i)

def heap_extract_min(heap):
    length=heap.length
    if(length<1):
        print("Heap Underfolw")
    else:
        min=heap.element[0]
        heap.element[0]=heap.element[length-1]
        heap.length=length-1
        min_heapify(heap,1)
        return min
def heap_sort(heap):
    sets=[]
    while(heap.length>0):
        min=heap_extract_min(heap)
        sets.append(min)
    return sets

class Heap():
    def __init__(self,setter=[]):
        self.element=[]
        if(len(setter)!=0):
            for i in setter:
                self.element.append(i)
        self.length=len(self.element)

heap=Heap([5, 7, 9, 4, 3,8])
# i=1
# min_heapify(heap,i)
build_min_heap(heap)
# print(heap)

# build_min_heap(heap)
print(heap.element)
# sets=heap_sort(heap)
# print(sets)
# print(heap_extract_min(heap))
# print(heap.element)
