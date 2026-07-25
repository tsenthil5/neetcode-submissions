class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def dfs(rowIdx, prevCol):
            if rowIdx >= len(points):
                return 0

            if (rowIdx, prevCol) in visited:
                return visited[(rowIdx, prevCol)]

            maxPoints = 0
            for idx, rowVal in enumerate(points[rowIdx]):
                if rowIdx != 0:
                    maxPoints = max(
                        maxPoints,
                        dfs(rowIdx+1, idx) + rowVal - abs(prevCol-idx)
                        )
                else:
                    maxPoints = max(
                        maxPoints,
                        dfs(rowIdx+1, idx) + rowVal
                        )

                

            visited[(rowIdx, prevCol)] = maxPoints
            return maxPoints

        visited = {}
        return dfs(0, 0)
        