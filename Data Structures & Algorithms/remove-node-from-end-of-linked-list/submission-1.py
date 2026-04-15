# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        count = 1

        while head.next:
            head = head.next
            count += 1
        
        index = count - n

        if index < 0:
            return start
        if index == 0:
            return start.next

        i = 0
        head = start
        prev = None
        future = head.next

        while i < index and future:
            prev = head
            head = head.next
            future = head.next
            i += 1

        prev.next = future
        return start