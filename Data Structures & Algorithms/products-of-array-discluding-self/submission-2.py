class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cache = 1    
        answer = []
        n = len(nums)
        for i in range(n):
            x = cache
            for j in range(i + 1, n):
                x *= nums[j]
            answer.append(x)
            cache *= nums[i]
        return answer