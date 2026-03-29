class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail
        self.head = Node()  # least recently used is right after head
        self.tail = Node()  # most recently used is right before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove a node from the list
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert a node right before tail (most recently used)
    def _insert_to_tail(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_to_tail(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_to_tail(node)

            if len(self.cache) > self.capacity:
                # remove least recently used (node right after head)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]