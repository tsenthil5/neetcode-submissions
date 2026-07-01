# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def gcd(num1, num2):
            maxNum = 1
            for i in range(1, min(num1, num2)+1):
                if num1 % i == 0 and num2 % i == 0:
                    maxNum = max(maxNum, i)

            return maxNum
        left, right = head, head.next

        while right != None:
            gcdNode = ListNode(gcd(left.val, right.val))
            left.next = gcdNode
            gcdNode.next = right
            left = right
            right = right.next


        return head
        