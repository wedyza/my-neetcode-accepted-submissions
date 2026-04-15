class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ex = None
        c = 0
        while head is not None:
            c += 1
            future = head.next
            head.next = ex
            ex = head
            head = future
        return ex

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        if head.next is None:
            return

        l1 = head
        l2 = head

        ex_l1 = l1
        while l2 is not None and l2.next is not None:
            ex_l1 = l1
            l1 = l1.next
            l2 = l2.next
            l2 = l2.next

        ex_l1.next = None
        
        tail = self.reverseList(l1)        
        res = head
        head = head.next
        while head is not None or tail is not None:
            print(f'b4 {res}')
            if tail is not None:
                future_tail = tail.next
                res.next = tail
                res = res.next
                tail = future_tail
                print(f'after 1 {res.val}')
            if head is not None:
                future_head = head.next
                res.next = head
                res = res.next
                print(f'after 2 {res.val}')
                head = future_head