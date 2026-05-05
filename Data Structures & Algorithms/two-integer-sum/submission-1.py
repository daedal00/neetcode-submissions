class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in prevMap:
                return [prevMap[compliment], i]
            else:
                prevMap[n] = i