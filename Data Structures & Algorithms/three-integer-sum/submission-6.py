class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ansSet = set()
        nums.sort()

        for i in range(len(nums) - 2):
            sumSet = set()
            for j in range(i+1, len(nums)):
                target = -1 * (nums[i] + nums[j])
                if target in sumSet:
                    triplet = tuple(sorted([nums[i] , target ,nums[j]]))
                    if triplet not in ansSet:
                        ans.append([nums[i] , target ,nums[j]])
                        ansSet.add(triplet)
                else:
                    sumSet.add(nums[j])
        return ans