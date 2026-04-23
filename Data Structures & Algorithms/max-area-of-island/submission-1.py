class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        res = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            size = 0
            while q:
                x, y = q.popleft()
                size += 1

                for step in range(-1, 2, 2):
                    dx = x + step
                    dy = y + step

                    if dx >= 0 and dx < rows and grid[dx][y] == 1 and not visited[dx][y]:
                        visited[dx][y] = True
                        q.append((dx, y))
                    if dy >= 0 and dy < cols and grid[x][dy] == 1 and not visited[x][dy]:
                        visited[x][dy] = True
                        q.append((x, dy))
            return size

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and not visited[x][y]:
                    res = max(res, bfs(x, y))
        
        return res