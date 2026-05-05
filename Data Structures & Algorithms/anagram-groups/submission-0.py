class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            soln[sortedWord].append(word)
        return list(soln.values())