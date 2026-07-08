class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            0
        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            if s[r] not in seen:
                seen.add(s[r])
            res = max(res, r - l + 1)
        return res