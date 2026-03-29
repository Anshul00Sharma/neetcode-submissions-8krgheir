class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSubArraySum = nums[0]
        currentSum = 0

        for el in nums:
            currentSum += el
            maxSubArraySum = max(maxSubArraySum,currentSum)
            currentSum = max(currentSum,0)
        return maxSubArraySum