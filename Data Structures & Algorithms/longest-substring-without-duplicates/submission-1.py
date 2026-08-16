class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # left = 0
        # res = 0

        # for right in range(len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left += 1
        #     charSet.add(s[right])
        #     res = max(res, right - left + 1)
        # return res

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res



        