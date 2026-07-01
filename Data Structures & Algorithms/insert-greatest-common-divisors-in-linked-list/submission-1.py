# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def gcd(num1, num2):
            while num2:
                num1,num2 = num2, num1%num2

            return num1
        left, right = head, head.next

        while right != None:
            gcdNode = ListNode(gcd(left.val, right.val))
            left.next = gcdNode
            gcdNode.next = right
            left = right
            right = right.next


        return head
        