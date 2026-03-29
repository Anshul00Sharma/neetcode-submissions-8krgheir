class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(n):
            count = 0
            it = n
            while it > 0:
                if it & 1 == 1:
                    count += 1
                it = it >> 1
            return count

        ans = []
        
        for i in range(n+1):
            ans.append(countOne(i))
        return ans

    
        