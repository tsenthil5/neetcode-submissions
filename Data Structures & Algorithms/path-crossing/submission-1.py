class Solution:
    def isPathCrossing(self, path: str) -> bool:



        directions = {
            "N": (0,1),
            "E": (1,0),
            "S": (0,-1),
            "W":(-1,0)
        }

        x = 0
        y = 0
        visited = set()
        visited.add((x,y))
        #print(visited)
        for char in path:
            x+=directions[char][0]
            y+=directions[char][1]
            #print(x, y)
            #print(visited)
            if (x,y) in visited:
                return True

            visited.add((x,y))


        return False



        