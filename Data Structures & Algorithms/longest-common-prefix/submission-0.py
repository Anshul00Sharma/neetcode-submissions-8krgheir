class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        count = 0
        while True:
            if count > len(strs[0]):
                return common
            common = strs[0][:count]
            for st in strs:
                if st[:count] != common:
                    return common[:count-1]
            count += 1    


        