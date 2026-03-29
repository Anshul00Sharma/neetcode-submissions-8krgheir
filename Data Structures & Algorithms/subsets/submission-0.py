class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def tracking(i: int):

            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            tracking(i + 1)

            subset.pop()
            tracking(i+1)
        tracking(0)
        return res
    

        