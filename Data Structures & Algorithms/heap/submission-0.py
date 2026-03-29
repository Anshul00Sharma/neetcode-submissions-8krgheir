class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up_(len(self.heap) - 1)


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down_(1)
        return res

    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]

    def _bubble_up_(self, index):
        heap = self.heap
        while index > 1:
            parent = index // 2
            if heap[parent] > heap[index]:
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent
            else:
                break

    def _bubble_down_(self, index):
        heap = self.heap
        while 2 * index < len(heap):
            smallest = 2 * index
            if smallest + 1 < len(heap) and heap[smallest + 1] < heap[smallest]:
                smallest += 1
            
            if heap[index] > heap[smallest]:
                heap[index], heap[smallest] = heap[smallest], heap[index]
                index = smallest
            else:
                break

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range((len(self.heap) - 1) // 2, 0, -1):
            self._bubble_down_(i)