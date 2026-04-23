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

        def dfs(i):
            if i == len(digits):
                res.append("".join(stack))
                return

            for j in range(len(mapping[digits[i]])):
                stack.append(mapping[digits[i]][j])
                dfs(i + 1)
                stack.pop()
        
        dfs(0)

        return res