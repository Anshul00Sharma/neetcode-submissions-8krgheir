class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None 

        length = 0
        move = head
        while move:
            move = move.next
            length += 1
        removeElementIndex = length - n
        
        if removeElementIndex == 0:
            return head.next

        removeElementNode = head
        prev = None
        while removeElementNode and removeElementIndex > 0:
            prev = removeElementNode
            removeElementNode = removeElementNode.next
            removeElementIndex -= 1
        
        nxt = removeElementNode.next 
        prev.next = nxt
        return head