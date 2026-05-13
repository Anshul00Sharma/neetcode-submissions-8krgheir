class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        minimum = nums[0]
        while low <= high:
            if nums[low] <= nums[high]:
                minimum = min(minimum,nums[low])
                return minimum
            mid = (low+high) // 2
            minimum = min(minimum,nums[mid])
            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return minimum