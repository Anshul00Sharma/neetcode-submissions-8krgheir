class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set()

        for el in nums:
            if el in cache:
                return True
            else:
                cache.add(el)
        return False


      
       