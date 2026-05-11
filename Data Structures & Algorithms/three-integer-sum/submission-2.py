class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cache = set()
            not_in = set()
            j = i+1
            target = -nums[i]
            while j < len(nums):
                val = target - nums[j]
                if val in cache:
                    ans = [nums[i],val,nums[j]]
                    if nums[j] not in not_in:
                        answer.append(ans)
                    not_in.add(nums[j])
                cache.add(nums[j])
                j+=1
        return answer