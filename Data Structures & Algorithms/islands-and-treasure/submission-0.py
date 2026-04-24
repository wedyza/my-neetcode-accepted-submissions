class Solution:
    def visit(self, grid, x, y, d):
        if x >= 0 and y >= 0 and x < self.dx and y < self.dy:    
            if grid[x][y] > d:
                grid[x][y] = d
                return True
            return grid[x][y] == 0
        return False

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        CHEST = 0
        WALL = -1

        q = deque()

        self.dx = len(grid)
        self.dy = len(grid[0])
        
        for x in range(self.dx):
            for y in range(self.dy):
                if grid[x][y] == 0:
                    q.append((x, y, 0))

                    while q:
                        x, y, d = q.popleft()
                        # print(x, y, grid[x][y])

                        if self.visit(grid, x + 1, y, d + 1):
                            q.append((x + 1, y, d + 1))
                        
                        if self.visit(grid, x - 1, y, d + 1):
                            q.append((x - 1, y, d + 1))

                        if self.visit(grid, x, y + 1, d + 1):
                            q.append((x, y + 1, d + 1))

                        if self.visit(grid, x, y - 1, d + 1):
                            q.append((x, y - 1, d + 1))
                        
                        