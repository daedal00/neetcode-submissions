class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            left = numbers[l]
            right = numbers[r]
            if left + right == target:
                return [l + 1, r + 1]
            if left + right > target:
                r -= 1
            if left + right < target:
                l += 1
        return []