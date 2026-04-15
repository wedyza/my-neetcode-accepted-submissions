from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []
        
        q = deque([(root, 0)])

        while q:
            root, layer = q.popleft()
            if not root:
                continue
            if len(layers) == layer:
                layers.append([root.val])
            else:
                layers[layer].append(root.val)
            
            q.append((root.left, layer + 1))
            q.append((root.right, layer + 1))
        
        return layers