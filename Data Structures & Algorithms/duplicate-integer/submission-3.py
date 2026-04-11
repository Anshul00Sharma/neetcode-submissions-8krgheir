class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()

        for el in nums:
            if el in prev:
                return True
            else:
                prev.add(el)
    
        return False
       