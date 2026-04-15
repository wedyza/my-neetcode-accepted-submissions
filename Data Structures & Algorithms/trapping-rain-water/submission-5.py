class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_prefixes = [height[0]]
        right_prefixes = [height[-1]]

        for i in range(1, n):
            left_prefixes.append(max(left_prefixes[i-1], height[i]))
            right_prefixes.append(max(right_prefixes[i-1], height[n - i - 1]))
        right_prefixes = right_prefixes[::-1]
        s = 0
        print(left_prefixes)
        print(right_prefixes)
        for i in range(1, n - 1):
            x = min(left_prefixes[i], right_prefixes[i]) - height[i]
            print(i, x)
            if x > 0:
                s += x
        
        return s