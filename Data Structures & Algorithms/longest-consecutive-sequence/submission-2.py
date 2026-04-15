class Solution:
    cache = {}

    def countConsecutive(self, number, nums):
        if number - 1 in self.cache.keys():
            self.cache[number] = self.cache[number - 1]  + 1
            return self.cache[number]
        if number - 1 in nums:
            return self.countConsecutive(number - 1, nums) + 1   
        return 1
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return max([self.countConsecutive(n, set(nums)) for n in nums])