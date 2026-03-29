class Solution:
    def hammingWeight(self, n: int) -> int:
        iterat = n
        count = 0
        while iterat > 0:
            if iterat & 1 == 1:
                count += 1
            iterat = iterat >> 1
        return count

        