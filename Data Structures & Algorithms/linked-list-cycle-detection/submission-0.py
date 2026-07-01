# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start, end = head, head.next
        while start!=end:
            if not end or not end.next:
                return False
            start = start.next
            end = end.next.next

        return True

        