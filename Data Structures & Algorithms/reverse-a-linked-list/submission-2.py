# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        elif not head.next:
            return head
        else:

            left, right = head, head.next
            while right:
                temp = right.next
                right.next = left
                left = right
                right = temp


            head.next = None

            return left

        