class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nodeA = head
        nodeB = head.next

        while nodeA and nodeB:
            if nodeA == nodeB:
                return True
            nodeA = nodeA.next
            if nodeB.next:
                nodeB = nodeB.next.next
            else:
                return False
        return False