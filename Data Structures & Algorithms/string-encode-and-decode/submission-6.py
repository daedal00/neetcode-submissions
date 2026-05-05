class Solution:

    # delimiter "# + len(word)"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            cur = str(len(word)) + "#" + word
            res += cur
        return res
    def decode(self, s: str) -> List[str]:
        # 2#hi4#test
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i= j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res