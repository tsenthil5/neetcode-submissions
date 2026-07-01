# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        BST-
            store nodes from an inorder traversal - sorted list

        kptr = 1
        dfs() - inorder traversal
            if kptr == k
                return node value

            kptr+=1

        '''
        kptr = 0
        kVal = None
        def dfs(node):
            nonlocal kptr, kVal
            if not node:
                return

            dfs(node.left)
            kptr+=1
            if kptr == k:
                kVal = node.val
                return
            dfs(node.right)


        dfs(root)
        return kVal


        












        