class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k=i+1,n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    val = [nums[i] , nums[j] , nums[k]]
                    ans.append(val)
                    while j < k and nums[j] == val[1]:
                        j += 1
                    while j < k and nums[k] == val[2]:
                        k -= 1
        
        return ans