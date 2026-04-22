class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(path, i):
            res.append(path.copy())
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                path.append(nums[j])
                dfs(path, j + 1)
                path.pop()

        dfs([], 0)
        return res