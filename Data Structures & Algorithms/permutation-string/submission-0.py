class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ns1 = len(s1)
        ns2 = len(s2)
        sorteds1 = sorted(s1)
        p1 = 0
        p2 = ns1

        while p2 <= ns2:
            substring = s2[p1:p2]
            sorteds2 = sorted(substring)
            if sorteds1 == sorteds2:
                return True
            p1 += 1
            p2 += 1
        return False