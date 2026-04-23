class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        res = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def visit(x, y):
            if x < 0 or y < 0 or x == rows or y == cols:
                return

            if grid[x][y] == '1':
                visited[x][y] = True
            else:
                return

            if x < rows - 1 and not visited[x+1][y]:
                visit(x + 1, y)
            if x > 0 and not visited[x-1][y]:
                visit(x - 1, y)
            if y < cols - 1 and not visited[x][y+1]:
                visit(x, y + 1)
            if y > 0 and not visited[x][y-1]:
                visit(x, y - 1)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and not visited[x][y]:
                    res += 1
                    visit(x, y)
        
        return res