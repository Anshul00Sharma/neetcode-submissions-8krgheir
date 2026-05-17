class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = node = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            plus = v1 + v2 + carry
            carry = plus // 10
            newNode = ListNode(plus % 10)
            node.next = newNode
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next