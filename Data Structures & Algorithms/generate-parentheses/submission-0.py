class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, opening, closing):
            if closing > opening or opening > n:
                return  
            if opening == closing and opening == n:
                res.append(string)
            b1 = string + "("
            dfs(b1, opening + 1, closing)
            b2 = string + ")"
            dfs(b2, opening, closing + 1)
        
        dfs("", 0, 0)
        return res