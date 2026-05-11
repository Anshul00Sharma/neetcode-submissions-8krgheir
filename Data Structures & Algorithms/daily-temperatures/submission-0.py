class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _,index = stack.pop()
                ans[index] = i - index
            stack.append([t,i])
        return ans