class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        

        def bfs(queue):
            while queue:
                lenQ = len(queue)
                directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
                for i in range(lenQ):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        newRow, newCol = r+dr, c+dc
                        if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                            if grid[newRow][newCol] == 2147483647:
                                grid[newRow][newCol] = grid[r][c]+1
                                queue.append((newRow, newCol))


        bfs(queue)

        