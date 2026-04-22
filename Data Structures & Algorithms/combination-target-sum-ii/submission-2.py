class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(csum, path, i):
            if csum > target:
                return

            if csum == target:
                res.append(path[:])
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if csum + candidates[j] > target:
                    break

                path.append(candidates[j])
                dfs(csum + candidates[j], path, j + 1)
                path.pop()
        
        dfs(0, [], 0)
        # return [list(c) for c in res]
        return res