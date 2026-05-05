class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = [0] * 26
        t_char = [0] * 26
        for i in range(len(s)):
            s_char[ord('a') - ord(s[i])] += 1
            t_char[ord('a') - ord(t[i])] += 1
        return s_char == t_char