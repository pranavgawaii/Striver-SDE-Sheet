class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        nex = dummy
        pre = dummy
        
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
            
        while count >= k:
            curr = pre.next
            nex = curr.next
            for i in range(1, k):
                curr.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = curr.next
            pre = curr
            count -= k
            
        return dummy.next
