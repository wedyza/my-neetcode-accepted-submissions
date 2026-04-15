class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                cache[(i, j)] = cache.get((i, j), 0) + 0 - (nums[i] + nums[j])

        for k in range(n):
            for i, j in cache.keys():
                if nums[k] == (cache[(i, j)]) and i != j and i != k and k != j:
                    p = sorted([nums[i], nums[j], nums[k]])
                    if p not in res:
                        res.append(p)
        return res