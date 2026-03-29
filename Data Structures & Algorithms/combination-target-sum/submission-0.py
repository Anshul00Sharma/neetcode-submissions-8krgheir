class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sumToNine = [] 

        def tracking(i:int):
            if sum(sumToNine) == target:
                res.append(sumToNine.copy())
                return

            if i >= len(nums) or sum(sumToNine) > target:
                return 
            
            sumToNine.append(nums[i])
            tracking(i)

            sumToNine.pop()
            tracking(i + 1)

        tracking(0)

        return res
