class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(csum, path):
            if csum > target:
                return
            if csum == target:
                p = sorted(path[:])
                res.add(tuple(p))
            
            for i in range(len(nums)):
                current_number = nums[i]
                csum += current_number
                path.append(current_number)
                dfs(csum, path)
                csum -= current_number
                path.pop()
        
        dfs(0, [])

        return [list(c) for c in res]