class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        cache = set(nums)
        for el in cache:
            while el - 1 in cache:
                el -= 1
            length = 0
            while el in cache:
                el += 1
                length += 1
            longest = max(longest,length)
        return longest