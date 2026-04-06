class MaxHeap:   
    def __init__(self):
        self.heap = []  # create an empty heap list

    # insert a new value into heap and moveup to keep heap right
    def insert(self, value):
        self.heap.append(value)
        self.moveup(len(self.heap) - 1)

    # build heap from an unsorted array by using bottom-up heap construction
    def build_heap(self, arr):
        self.heap = arr[:]

        # start from last non-leaf node
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.movedown(i)

    # remove and return the max value (root) then rearrange the heap to keep max-heap structure
    def removemax(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]

        # move last element to root
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # restore heap property
        self.movedown(0)

        return max_value


    # move the value up if it is larger than parent
    def moveup(self, i):
        parent = (i-1)//2

        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

            i = parent
            parent = (i-1)//2

    # move the value down if it is smaller than children
    def movedown(self, i): #maxheap

        size = len(self.heap)

        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
