# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertNode(self, node):
        buffer = node.left
        node.left = node.right
        node.right = buffer
        if node.left:
            self.invertNode(node.left)
        if node.right:
            self.invertNode(node.right)
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertNode(root)
        return root