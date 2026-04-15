class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        n = 1
        for c, i in enumerate(nums):
            if c > 0:
                prefix.append(n)
            else:
                prefix.append(1)
            n *= i
            
        
        n = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix.append(1)
            else:
                suffix.append(n)
            
            n *= nums[i]
        suffix = suffix[::-1]

        return [suffix[i] * prefix[i] for i in range(len(nums))]