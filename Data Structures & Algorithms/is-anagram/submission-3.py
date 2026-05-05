class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dictS, dictT = {}, {}
        for c in s:
            dictS[c] = dictS.get(c, 0) + 1
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        return dictT == dictS