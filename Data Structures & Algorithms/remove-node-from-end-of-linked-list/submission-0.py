# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        [1,2,3,4]

        '''

        start, end = head, head

        while n!=0:
            end = end.next
            n-=1


        if not end:
            return start.next

        while end.next != None:
            start = start.next
            end = end.next

        start.next = start.next.next

        return head
        