class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        n = len(nums)

        for i in range(n):
            x = target - nums[i];
            if x in hash.keys():
                return [hash[x], i]
            hash[nums[i]] = i
