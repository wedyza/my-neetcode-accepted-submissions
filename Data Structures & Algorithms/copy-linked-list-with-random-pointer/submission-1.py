"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}
        flag = True
        res = head
        while head:
            copy = Node(head.val)
            if flag:
                res = copy
                flag = False
            d[head] = copy
            head = head.next
        print(d)
        for key in d:
            if key:
                original = d[key]
                next_value = d[key.next]
                random_value = d[key.random]
                original.next = next_value
                original.random = random_value
        
        return res