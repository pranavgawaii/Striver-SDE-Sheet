class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        
        # step 1: insert cloned nodes in between original nodes
        curr = head
        while curr:
            clone = Node(curr.val)
            clone.next = curr.next
            curr.next = clone
            curr = clone.next
        
        # step 2: assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # step 3: separate original and cloned lists
        dummy = Node(0)
        clone_curr = dummy
        curr = head
        while curr:
            clone_curr.next = curr.next
            curr.next = curr.next.next
            clone_curr = clone_curr.next
            curr = curr.next
        
        return dummy.next
