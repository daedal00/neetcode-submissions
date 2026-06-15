class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ordMap = [0] * 26
            for c in s:
                ordMap[ord(c) - ord('a')] += 1
            res[tuple(ordMap)].append(s)
        return list(res.values())