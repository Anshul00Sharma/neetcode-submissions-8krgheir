class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            cache = set()
            not_in_use = set()
            target = -nums[i]
            while j < len(nums):
                val = target - nums[j]
                if val in cache:
                    ans = [nums[i],val,nums[j]]
                    if nums[j] not in not_in_use:
                        answers.append(ans)
                    not_in_use.add(nums[j])
                cache.add(nums[j])
                j+=1
        return answers

               
                
        