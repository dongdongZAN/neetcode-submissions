class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeList = []
        for s in strs:
            encodeList.append(str(len(s)))
            encodeList.append("#")
            encodeList.append(s)
        return "".join(encodeList)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
