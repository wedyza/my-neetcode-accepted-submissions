class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = set()
        n = len(nums)
        def dfs(path):
            res.add(tuple(sorted(path.copy())))

            for key in d:
                if d[key] > 0:
                    path.append(key)
                    d[key] -= 1
                    dfs(path)
                    d[key] += 1
                    path.pop()
        dfs([])
        return [list(c) for c in res]