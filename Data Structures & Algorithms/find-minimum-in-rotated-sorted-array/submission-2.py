class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l = 0
        r = n - 1
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] < nums[0]:
                r = middle - 1
            else:
                l = middle + 1
        return nums[l]