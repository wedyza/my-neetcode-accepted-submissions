class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for c, i in enumerate(nums):
            if c > 0 and nums[c-1] == nums[c]:
                continue
            
            l = c + 1
            r = len(nums) - 1
            while l < r:
                target = i + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([i, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res