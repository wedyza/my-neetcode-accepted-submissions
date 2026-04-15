# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = 0
        answer = 0

        def dfs(root):
            nonlocal current, answer
            if not root:
                return
            dfs(root.left)
            
            current += 1
            # print(current, k)
            if current == k:
                answer = root.val
                raise BaseException
            
            dfs(root.right)

        try:
            dfs(root)
        finally:
            return answer