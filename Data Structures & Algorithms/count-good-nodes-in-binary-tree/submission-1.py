# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0

        def dfs(root, most):
            nonlocal res
            if not root:
                return
            if root.val >= most:
                res += 1
                most = root.val
            dfs(root.left, most)
            dfs(root.right, most)
        dfs(root, root.val)
        return res