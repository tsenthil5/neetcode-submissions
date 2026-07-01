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
        kptr = 1
        def dfs(node):
            nonlocal kptr
            if not node:
                return -1

            leftChild = dfs(node.left)
            if leftChild != -1:
                return leftChild
            if kptr == k:
                return node.val
            kptr+=1
            rightChild = dfs(node.right)
            if rightChild != -1:
                return rightChild
            
            return -1


        return dfs(root)


        












        