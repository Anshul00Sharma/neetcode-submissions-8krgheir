class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sq = set()

        for el in nums:
            sq.add(el)
        maxc = 0
        
        for el in nums:
            firstEl = el
            localmax = 0 
            if (firstEl - 1) not in sq:
                while firstEl in sq:
                    firstEl = firstEl + 1
                    localmax += 1
                maxc = max(localmax,maxc)
        return maxc