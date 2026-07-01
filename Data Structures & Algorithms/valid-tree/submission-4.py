class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMat = defaultdict(list)
        
        for node1, node2 in edges:
            adjMat[node1].append(node2)

        def dfs(node):
            
            if node in visited:
                return False
            visited.add(node)
            if adjMat[node] == []:
                return True
            for child in adjMat[node]:
                if dfs(child) == False:
                    return False

            return True


        visited = set()
        if dfs(0) == False:
            return False
        for key in list(adjMat.keys()):
            if key not in visited:
                return False
        return True        