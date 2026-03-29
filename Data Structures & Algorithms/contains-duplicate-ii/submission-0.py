class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        sack = {}

        for r in range(len(nums)):
            if r-l > k:
                sack.pop(nums[l])
                l += 1
            if nums[r] in sack:
                return True
            sack[nums[r]] = 1

        return False