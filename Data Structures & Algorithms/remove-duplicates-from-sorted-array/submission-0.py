class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sortedPointer = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] != nums[i]:
                sortedPointer += 1
                nums[sortedPointer] = nums[i]
        return sortedPointer + 1