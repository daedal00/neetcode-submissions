class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curs = set()
        for n in nums:
            if n in curs:
                return True
            else:
                curs.add(n)
        return False