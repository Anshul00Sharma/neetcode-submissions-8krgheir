class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = [*nums]
        for i in nums:
            newArr.append(i)  
        return newArr
        