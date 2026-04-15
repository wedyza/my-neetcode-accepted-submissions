class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        for i in range(1, n - 1):
            left = max(height[:i])
            right = max(height[i+1:])
            amount = min(left, right) - height[i]
            if amount > 0:
                s += amount
        return s