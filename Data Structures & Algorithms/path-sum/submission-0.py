# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        


        def pathSum(node, currPathSum):
            if not node:
                return False
            if not node.left and not node.right:
                if currPathSum+node.val == targetSum:
                    return True

            
            

            if (pathSum(node.left, currPathSum+node.val) or pathSum(node.right, currPathSum+node.val)):
                return True
            


            return False


        return pathSum(root, 0)
        