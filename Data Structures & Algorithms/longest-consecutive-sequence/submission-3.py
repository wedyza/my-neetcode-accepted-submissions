class Solution:
    cache = {}

    def countConsecutive(self, number, nums):
        if number in self.cache.keys():
            return self.cache[number]
        if number - 1 in self.cache.keys():
            self.cache[number] = self.cache[number - 1]  + 1
            return self.cache[number]
        if number - 1 in nums:
            c = self.countConsecutive(number - 1, nums) + 1
            self.cache[number] = c
            return c
        self.cache[number] = 1
        return 1
    
    def longestConsecutive(self, nums: List[int]) -> int:
        self.cache = {}
        if len(nums) == 0:
            return 0
        return max([self.countConsecutive(n, set(nums)) for n in nums])