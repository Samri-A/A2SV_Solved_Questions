"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        new_graph = {}

        def dfs(node):

            if node in new_graph:
                return new_graph[node]

            cloned_node = Node(node.val)
            new_graph[node] = cloned_node

            for neb in node.neighbors:
                
                cloned_node.neighbors.append(dfs(neb))
            
            return cloned_node

        
        return dfs(node)
        
