# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)
        

    def helper(self,head):
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.helper(head.next)
            nxt = head.next
            nxt.next = head
        head.next = None
        return newHead
   

