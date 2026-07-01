# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        count = 0
        def countGoodNodes(root, largest):
            nonlocal count
            if not root:
                return
            countGoodNodes(root.left, max(root.val, largest))
            if root.val >= largest:
                count+=1
            countGoodNodes(root.right, max(root.val, largest))


        
        countGoodNodes(root, float('-inf'))
        return count

        
        