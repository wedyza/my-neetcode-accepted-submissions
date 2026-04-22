class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opening, closing):
            if closing > opening or opening > n:
                return  
            if opening == closing and opening == n:
                res.append("".join(stack))
            stack.append("(")
            dfs(opening + 1, closing)
            stack.pop()
            stack.append(")")
            dfs(opening, closing + 1)
            stack.pop()
        
        dfs(0, 0)
        return res