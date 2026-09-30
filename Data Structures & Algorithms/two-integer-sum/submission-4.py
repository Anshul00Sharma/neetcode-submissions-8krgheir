class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for index in range(len(nums)):
            if target - nums[index] in prev:
                return [prev[target - nums[index]] , index]
            prev[nums[index]] = index
        return []            
        