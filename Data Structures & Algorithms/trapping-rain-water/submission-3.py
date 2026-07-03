class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxLeft = [0] * len(height)
        curLeft = 0
        maxRight = [0] * len(height)
        curRight = 0
        for l in range(len(height)):
            curLeft = max(curLeft, height[l])
            maxLeft[l] = curLeft
        for r in range(len(height)-1, -1, -1):
            curRight = max(curRight, height[r])
            maxRight[r] = curRight
        
        res = 0
        for i in range(len(height)):
            area = min(maxLeft[i], maxRight[i]) - height[i]
            if area > 0:
                res +=  area
        return res