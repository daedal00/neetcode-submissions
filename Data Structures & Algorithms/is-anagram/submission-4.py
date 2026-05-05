class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = [0] * 26
        for c in s:
            charMap[ord(c) - ord('a')] += 1
        for c in t:
            charMap[ord(c) - ord('a')] -= 1
        return all(v == 0 for v in charMap)