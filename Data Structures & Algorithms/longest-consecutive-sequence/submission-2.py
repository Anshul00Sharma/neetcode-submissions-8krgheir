class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set()

        for n in nums:
            numberset.add(n)
        maxlength = 0
        for element in numberset:
            if element - 1 in numberset:
                continue
            curl = 0
            while element in numberset:
                curl += 1
                element += 1
            maxlength = max(maxlength,curl)
        return maxlength    
             
        