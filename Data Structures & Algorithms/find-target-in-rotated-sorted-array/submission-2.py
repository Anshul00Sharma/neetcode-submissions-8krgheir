class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2             # middle index
            if target == nums[m]:
                return m

            # If the left half (from l to m) is sorted in ascending order
            if nums[l] <= nums[m]:
                # Check if target lies in this sorted left half.
                # Targets must be between nums[l] and nums[m] (inclusive on left, exclusive on right).
                if nums[l] <= target < nums[m]:
                    h = m - 1            # move to left half
                else:
                    l = m + 1            # target is in the rotated right half
            # Otherwise, the right half (from m to h) must be sorted
            else:
                # Check if target lies in the sorted right half.
                # Target must be strictly greater than nums[m] and <= nums[h].
                if nums[m] < target <= nums[h]:
                    l = m + 1            # move to right half
                else:
                    h = m - 1            # target is in the rotated left half
        return -1       