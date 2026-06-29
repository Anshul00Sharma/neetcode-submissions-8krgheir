class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashq = {}

        for i in range(len(nums)):
            if target - nums[i] in hashq:
                return [hashq[target - nums[i]] ,i]
            hashq[nums[i]] = i
        return []
        