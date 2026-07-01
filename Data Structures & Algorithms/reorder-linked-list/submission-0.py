# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        mid = slow
        ptr1, ptr2 = slow, slow.next
        while ptr2:
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp

        mid.next = None
        end = ptr1
        start = head
        while end != mid:
            tempEnd = end.next
            tempStart = start.next
            start.next = end
            end.next = tempStart
            start = tempStart
            end = tempEnd

        

        