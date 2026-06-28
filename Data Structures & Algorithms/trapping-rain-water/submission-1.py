class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        res = []
        curLeft = 0
        curRight = 0
        for i in range(len(height)):
            maxLeft[i] = curLeft
            curLeft = max(height[i], curLeft)
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = curRight
            curRight = max(height[i], curRight)
        
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water < 0:
                water = 0
            res.append(water)
        return sum(res)
