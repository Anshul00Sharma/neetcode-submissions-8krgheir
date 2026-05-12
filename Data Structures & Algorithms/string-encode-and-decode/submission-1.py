class Solution:

    def encode(self, strs: List[str]) -> str:
        codedMsg = ""
        for st in strs:
            codedMsg += f"{len(st)}#{st}"
        return codedMsg
        

    def decode(self, s: str) -> List[str]:
        strs = []
        p = 0
        while p < len(s):
            hashindex = s.find('#',p)
            length = int(s[p:hashindex])
            string = s[hashindex + 1: hashindex + 1 + length]
            strs.append(string)
            p = hashindex + 1 + length

        return strs
