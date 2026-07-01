# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(queue):
            if not queue[0]:
                return []
            res = []
            while queue:
                lenQ = len(queue)
                curr = []
                for i in range(lenQ):
                    root = queue.pop()
                    curr.append(root.val)
                    if root.left:
                        queue.insert(0,root.left)

                    if root.right:
                        queue.insert(0,root.right)

                res.append(curr)

            return res


        return bfs([root])
                    

                    









        