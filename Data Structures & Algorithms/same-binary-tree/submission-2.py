# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                return
            if root.left:
                res.append(root.left.val)
                dfs(root.left)
            else:
                res.append(None)
            
            if root.right:
                res.append(root.right.val)
                dfs(root.right)
            else:
                res.append(None)

        dfs(q)
        arr1 = res[:]
        res =[]
        dfs(p)
        print(arr1, res)
        return arr1 == res and ((not q and not p) or q.val == p.val)
            