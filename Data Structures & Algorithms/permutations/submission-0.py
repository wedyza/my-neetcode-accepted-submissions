class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = []
        n = len(nums)
        def dfs(path):
            if len(path) == n:
                res.append(path.copy())

            for key in d:
                if d[key] > 0:
                    path.append(key)
                    d[key] -= 1
                    dfs(path)
                    d[key] += 1
                    path.pop()
        dfs([])
        return res