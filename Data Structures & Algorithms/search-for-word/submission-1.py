class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = len(board)
        dy = len(board[0])
        visited = [[False for _ in range(dy)] for _ in range(dx)]

        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if x < 0 or y < 0 or x >= dx or y >= dy or word[i] != board[x][y] or visited[x][y]:
                return False
            
            visited[x][y] = True
            res = dfs(x + 1, y, i + 1) or dfs(x - 1, y, i + 1) or dfs(x, y + 1, i + 1) or dfs(x, y - 1, i + 1)
            visited[x][y] = False
            return res
        
        for i in range(dx):
            for j in range(dy):
                if dfs(i, j, 0):
                    return True
        
        return False