class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')
        n = len(heights)
        l = 0
        r = n -1
        while l < r:
            target = (r - l) * min(heights[l], heights[r])
            res = max(target, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res