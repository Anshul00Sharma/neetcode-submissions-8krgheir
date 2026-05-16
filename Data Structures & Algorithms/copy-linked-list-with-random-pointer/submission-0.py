class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        firstPass = head
        dummy = node =  Node(0)
        maping = {None: None}

        while firstPass:
            newNode = Node(firstPass.val)
            maping[firstPass] = newNode
            node.next = newNode
            node = node.next
            firstPass = firstPass.next
        
        secondPass = head

        while secondPass:
            copyNode = maping[secondPass]
            linkedNode = maping[secondPass.random]
            copyNode.random = linkedNode
            secondPass = secondPass.next
        
        return dummy.next