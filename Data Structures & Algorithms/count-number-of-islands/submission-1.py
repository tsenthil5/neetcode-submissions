class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        backtracking solution
            O(M*N)
            visited (avoid duplicates)

        iterating throguh grid
            check if land/water
                if land
                    continue
                else
                return

        '''
        def dfs(row, col):
            
            if row < 0 or row >= len(grid) or col >= len(grid[0]) or col < 0:
                return

            if grid[row][col] == "0":
                return
            if (row, col) in visited:
                return 
            visited.add((row,col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)



        visited = set()
        numOfIsland = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    numOfIsland+=1

        return numOfIsland



        
        