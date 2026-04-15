from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([(root, 0)])
        
        last = (root.val, 0)
        # print(q, q.popleft()[1])
        while q:
            node, layer = q.popleft()
            if not node:
                continue
            
            if layer > last[1]:
                print(node.val, layer, last[0], last[1])
                res.append(last[0])
            last = (node.val, layer)
            q.append((node.left, layer + 1))
            q.append((node.right, layer + 1))
        
        res.append(last[0])

        return res

