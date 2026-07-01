class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMat = defaultdict(list)
        for e1, e2 in edges:
            adjMat[e1].append(e2)
            adjMat[e2].append(e1)

        def dfs(node):
            if not adjMat[node]:
                return 1
            if node in visited:
                return 0

            visited.add(node)
            for children in adjMat[node]:
                dfs(children)

            return 1




        visited = set()
        connected_comp = 0
        for node in range(n):
            connected_comp += dfs(node)

        return connected_comp
        