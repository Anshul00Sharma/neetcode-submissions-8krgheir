class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return pairs
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def helper(self,pairs,left,right):
        if left >= right:
            return None
        mid = (left + right) // 2
        self.helper(pairs, left,mid)
        self.helper(pairs,mid+1,right)
        self.merge(pairs,left,mid,right)
    
    def merge(self,pairs,left,mid,right):
        temp = []
        lp = left
        rp = mid + 1
        while lp <= mid and rp <= right:
            if pairs[lp].key <= pairs[rp].key:
                temp.append(pairs[lp])
                lp += 1
            else:
                temp.append(pairs[rp])
                rp+=1
        while lp <= mid:
            temp.append(pairs[lp])
            lp += 1
        while rp <= right:
            temp.append(pairs[rp])
            rp += 1
        for i in range(len(temp)):
            pairs[left + i] = temp[i]