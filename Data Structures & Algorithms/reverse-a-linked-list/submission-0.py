# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head


        head1 ,head2 = head, head.next
        newHead = head1
        while head1 and head2:
            temp = head2.next
            head2.next = head1
            head1 = head2
            head2 = temp


        newHead.next = None
        return head1

'''
0 <- 1 <- 2 -3
     h1.  h2




'''


        

        