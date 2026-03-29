class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for el in nums:
            if el in hashMap:
                return True
            else:
                hashMap[el] = 1
        return False
        