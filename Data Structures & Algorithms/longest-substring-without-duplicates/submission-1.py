class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        res_map = {}

        for r in range(len(s)):
            if s[r] in res_map:
                l = max(res_map[s[r]]+1, l)
            res_map[s[r]] = r
            res = max(res, r - l +1)
        return res