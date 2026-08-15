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
            return node
            
        clones = {}        
        q = deque()
        q.append(node)
        clones[node.val] = Node(node.val)        
        root = clones[node.val]
        while q:
            n = q.popleft()
            for nb in n.neighbors:
                if nb.val in clones:
                    continue
                clones[nb.val] = Node(nb.val)
                q.append(nb)

        q = deque()
        q.append(node)        
        visited = set()
        visited.add(node.val)
        while q:
            n = q.popleft()
            clone = clones[n.val]
            clone.neighbors = []
            
            for nb in n.neighbors:
                clone.neighbors.append(clones[nb.val])

                if nb.val in visited:
                    continue
                visited.add(nb.val)
                q.append(nb)

        return root



