class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ansArray = []

        for p1 in range(len(nums)-2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            p2 = p1 + 1
            visited = set()
            visitedTriplet = set()
            while p2 < len(nums):
                target = (nums[p1] + nums[p2]) * -1
                if target in visited:
                    ans = [nums[p1],target,nums[p2]]
                    if tuple(ans) not in visitedTriplet:
                        ansArray.append(ans)
                    visitedTriplet.add(tuple(ans))
                visited.add(nums[p2])
                p2 += 1
        return ansArray
        

