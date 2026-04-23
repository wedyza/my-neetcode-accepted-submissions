class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        stack = []
        n = len(digits)
        def dfs(i):
            if i == n:
                res.append("".join(stack))
                return

            rng = 4 if digits[i] == '7' or digits[i] == '9' else 3
            for j in range(rng):
                stack.append(mapping[digits[i]][j])
                dfs(i + 1)
                stack.pop()
        
        dfs(0)

        return res