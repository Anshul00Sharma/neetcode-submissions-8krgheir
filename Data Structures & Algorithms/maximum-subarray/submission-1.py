class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsubArray = nums[0]
        current = 0

        for el in nums:
            current += el
            maxsubArray = max(maxsubArray,current)
            current = max(current,0)
        return maxsubArray