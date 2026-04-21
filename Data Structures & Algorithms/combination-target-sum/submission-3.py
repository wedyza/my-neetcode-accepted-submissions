class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(i, csum, path):
            if csum > target:
                return
            if csum == target:
                p = sorted(path[:])
                res.add(tuple(p))
            
            for j in range(i, len(nums)):
                current_number = nums[j]
                csum += current_number
                path.append(current_number)
                dfs(j, csum, path)
                csum -= current_number
                path.pop()
        
        dfs(0, 0, [])

        return [list(c) for c in res]