class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = nums[0]
        for el in nums:
            if el < minElement:
                minElement = el
                break
        return minElement
        