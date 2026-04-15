from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqual(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        
        stack = [root]
        while stack:
            root = stack.pop()
            if root.val == subRoot.val:
                if self.isEqual(root, subRoot):
                    return True

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        return False