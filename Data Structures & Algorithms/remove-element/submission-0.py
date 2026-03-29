class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                p1 += 1
                count += 1 
                nums[p1] = nums[i]
        return count
            
        