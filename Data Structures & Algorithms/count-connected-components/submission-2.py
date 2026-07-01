class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMat = defaultdict(list)
        for node1, node2 in edges:
            adjMat[node1].append(node2)
            adjMat[node2].append(node1)


        def dfs(node):
            if adjMat[node] == []:
                return 

            if node in visited:
                return 

            visited.add(node)
            for child in adjMat[node]:
                dfs(child)
        


        connected = 0
        visited = set()
        for node in list(adjMat.keys()):
            if node not in visited:
                dfs(node)
                connected+=1
        if len(visited) == 0:
            return n
        return connected



        """
        {
            0:[1]
            1:[2]
            2:[3]
            3:[0]
            4:[5]
            6:[7]
            7:[4]
            8:[9]
            10:[11]
        }
        """