# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, k, stack):
            if root:      
                stack.append(root)

                if root.val == k.val:
                    return True

                if dfs(root.left, k, stack) or dfs(root.right, k, stack):
                    return True

                stack.pop()
                return False
            return False
        
        stack1 = []
        stack2 = []

        dfs(root, p, stack1)
        dfs(root, q, stack2)

        point = 0
        while point < len(stack1) and point < len(stack2) and stack1[point] == stack2[point]:
            point += 1
        
        return stack1[point - 1]