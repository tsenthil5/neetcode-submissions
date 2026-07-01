# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:




        def calculateMoney(root):
            if not root:
                return [0,0]

            leftrob, leftNotrob = calculateMoney(root.left)
            rightrob, rightNotrob = calculateMoney(root.right)
            
            rob = root.val + leftNotrob + rightNotrob

            notrob = max(leftrob,leftNotrob) + max(rightrob,rightNotrob)
            return [rob,notrob]

            
        return max(calculateMoney(root))

            



        