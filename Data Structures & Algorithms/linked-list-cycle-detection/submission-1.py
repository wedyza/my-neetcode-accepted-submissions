# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is not None:
            p1 = head.next
            if p1.next is not None:
                p2 = p1.next
            else:
                return False
        else:
            return False
        while p1 is not None and p2 is not None:
            if p1 == p2:
                return True
            
            if p1.next is not None:
                p1 = p1.next
            else:
                return False

            if p2.next is not None:
                p2 = p2.next
                if p2.next is not None:
                    p2 = p2.next
                else:
                    return False
            else:
                return False
        return False