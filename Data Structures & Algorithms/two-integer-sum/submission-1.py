class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}

        for i in range(len(nums)):
            if target - nums[i] in saved:
                return [saved[target - nums[i]] ,i]
            else:
                saved[nums[i]] = i
        return []

        