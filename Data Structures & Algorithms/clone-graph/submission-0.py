"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        res = Node(node.val)

        graphs = {node.val:res}

        def dfs(remote, local):
            print(remote.val)
            for another_node in remote.neighbors:
                if another_node.val in graphs:
                    local.neighbors.append(graphs[another_node.val])
                else:
                    local_node = Node(another_node.val)
                    local.neighbors.append(local_node)
                    graphs[another_node.val] = local_node
                    dfs(another_node, local_node)
        
        dfs(node, res)
        return res