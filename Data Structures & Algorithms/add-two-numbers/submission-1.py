class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ans = res

        f = False
        up = 0
        while l1 or l2 or up == 1:
            if f:
                print("DONE")
                res.next = ListNode()
                res = res.next
            else:
                f = True
            first_digit = l1.val if l1 else 0
            second_digit = l2.val if l2 else 0
            score = first_digit + second_digit
            carry = 1 if up == 1 else 0
            if score + carry >= 10:
                score -= 10
                up = 1
            else:
                up = 0
            
            res.val = score + carry
            print(res.val)
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
            print(res.next)
        
        return ans