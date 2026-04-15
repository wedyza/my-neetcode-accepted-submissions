# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ex = None
        while head is not None:
            future = head.next
            head.next = ex
            ex = head
            head = future
        return ex