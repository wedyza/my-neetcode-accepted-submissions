class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                b = j - i
                a = min(heights[i], heights[j])
                res = max(a*b, res)
        
        return res