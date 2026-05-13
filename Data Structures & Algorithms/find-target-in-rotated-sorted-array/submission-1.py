class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            if target == nums[m]:
                return m
            # determine which side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1