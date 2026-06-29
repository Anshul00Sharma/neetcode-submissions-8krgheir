class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for st in strs:
            coded += str(len(st)) + '#' + st
        return coded


    def decode(self, s: str) -> List[str]:
        decoded = []
        p = 0
        while p < len(s):
            hashindex = s.find('#', p)
            l = int(s[p:hashindex])
            decoded.append(s[hashindex+1: (hashindex+1)+l])
            p = (hashindex+1)+l
        return decoded