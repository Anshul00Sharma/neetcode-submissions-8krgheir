class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ansArray = [1] * len(nums)
        # prefix 
        prefix = 1
        for i in range(len(nums)):
            ansArray[i] = prefix
            prefix *= nums[i]
        
        # postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, - 1):
            ansArray[i] *= postfix
            postfix *= nums[i]
        return ansArray