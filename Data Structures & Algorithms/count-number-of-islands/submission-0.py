class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        def countIslands(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            if (row, col) in visited:
                return False

            if grid[row][col] != "1":
                return False

            
            visited.add((row,col))
            countIslands(row+1, col)
            countIslands(row-1, col)
            countIslands(row, col+1)
            countIslands(row, col-1)

        count = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    countIslands(row, col)
                    count+=1   

        return count     