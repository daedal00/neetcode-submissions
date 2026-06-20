class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            tmp = nums[i]
            res[i] *= prefix
            prefix *= tmp
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            tmp = nums[i]
            res[i] *= suffix
            suffix *= tmp
        return res