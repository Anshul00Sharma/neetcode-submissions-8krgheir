import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newheap = [-el for el in nums]
        heapq.heapify(newheap)

        for _ in range(k-1):
            if len(nums) > 0:
                heapq.heappop(newheap)
            else:
                break

        
        return -heapq.heappop(newheap) if nums and len(nums) > 0 else -1
