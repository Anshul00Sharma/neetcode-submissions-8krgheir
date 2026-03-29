import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, len(nums) - k, 0, len(nums) - 1)

    def quickSelect(self, nums, k, low, high) -> int:
        if low >= high:
            return nums[low]
        mid = self.mid(nums, low, high)
        if mid == k:
            return nums[mid]
        elif mid < k:
            return self.quickSelect(nums, k, mid + 1, high)
        else:
            return self.quickSelect(nums, k, low, mid - 1)
    
    def mid(self, nums, low, high) -> int:
        pv = high
        left = low
        move = low
        while move < pv:
            if nums[move] <= nums[pv]:
                nums[left], nums[move] = nums[move], nums[left]
                left += 1
            move += 1
        
        nums[left], nums[pv] = nums[pv], nums[left]
        return left