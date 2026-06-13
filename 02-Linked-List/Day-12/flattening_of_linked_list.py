class Node:
    def __init__(self, val=0, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom

class Solution:
    def flatten(self, root: Node) -> Node:
        if not root or not root.next:
            return root
        
        # recursively flatten the rest of the list
        root.next = self.flatten(root.next)
        
        # merge current list with the flattened next list
        root = self._merge(root, root.next)
        
        return root
    
    def _merge(self, a: Node, b: Node) -> Node:
        if not a:
            return b
        if not b:
            return a
        
        if a.val <= b.val:
            result = a
            result.bottom = self._merge(a.bottom, b)
        else:
            result = b
            result.bottom = self._merge(a, b.bottom)
        
        result.next = None
        return result
