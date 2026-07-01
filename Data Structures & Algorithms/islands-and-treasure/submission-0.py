class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(queue,visited):
            dist = 0
            while queue:
                lenq = len(queue)
                for i in range(lenq):
                    row, col = queue.pop()
                    grid[row][col] = dist
                    if row+1<len(grid) and (row+1, col) not in visited and grid[row+1][col]!=-1:
                        
                        #res[row+1][col] = dist
                        visited.add((row+1,col))
                        queue.insert(0, (row+1, col))
                        
                    if col+1<len(grid[0]) and (row, col+1) not in visited and grid[row][col+1]!=-1:
                        
                        #res[row][col+1] = dist
                        visited.add((row,col+1))
                        queue.insert(0, (row, col+1))
                        
                    if row-1>=0 and (row-1, col) not in visited and grid[row-1][col]!=-1:
                        
                        #res[row-1][col] = dist
                        visited.add((row-1,col))
                        queue.insert(0, (row-1, col))
                        
                    if col-1>=0 and (row, col-1) not in visited and grid[row][col-1]!=-1:
                        
                        #res[row][col-1] = dist
                        visited.add((row,col-1))
                        queue.insert(0, (row, col-1))
                dist+=1
            return res
               
            
               
     
        queue = []   
        visited = set()
        res = [[-1]*len(grid[0])]*len(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.insert(0, (row,col))
                    visited.add((row,col))
        
        bfs(queue,visited)
        return grid

        