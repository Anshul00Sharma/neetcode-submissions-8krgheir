class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        n = len(numbers)

        for i in range(n):
            if target - numbers[i] in cache:
                return [cache[target - numbers[i]]+1,i+1]
            cache[numbers[i]] = i
        return []