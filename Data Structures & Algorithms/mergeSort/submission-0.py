class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def helper(self, pairs, low, high):
        if low >= high:
            return
        
        mid = (high + low) // 2
        self.helper(pairs, low, mid)
        self.helper(pairs, mid + 1, high)
        self.merge(pairs, low, mid, high)
    
    def merge(self, pairs, low, mid, high):
        temp = []
        leftSt  = low
        rightSt = mid + 1
        while leftSt <= mid and rightSt <= high:
            if pairs[leftSt].key <= pairs[rightSt].key:
                temp.append(pairs[leftSt])
                leftSt += 1
            else:
                temp.append(pairs[rightSt])
                rightSt += 1
            
        while leftSt <= mid:
            temp.append(pairs[leftSt])
            leftSt += 1
        
        while rightSt <= high:
            temp.append(pairs[rightSt])
            rightSt += 1
        
        for i in range(len(temp)):
            pairs[low + i] = temp[i]