class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        res = nums[0]
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res