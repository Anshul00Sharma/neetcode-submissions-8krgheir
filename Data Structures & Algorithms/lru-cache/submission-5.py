class Node:
    def __init__(self,key,val,left=None,right=None) -> None:
        self.val = val
        self.key = key
        self.left = left
        self.right = right
        
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.right = self.right
        self.right.left = self.left

    def remove(self,node:Node):
        node.left.right = node.right
        node.right.left = node.left 

    def insert(self,node:Node):
        prev, nxt = self.right.left, self.right
        prev.right = nxt.left = node
        node.left, node.right = prev, nxt
        

    def get(self, key: int) -> int:
        if key in self.storage:
            self.remove(self.storage[key])
            self.insert(self.storage[key])
            return self.storage[key].val
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage[key].val = value
            self.remove(self.storage[key])
            self.insert(self.storage[key])
        else:
            if len(self.storage) >= self.capacity:
                lru = self.left.right
                self.remove(lru)
                del self.storage[lru.key]
            
            new_node = Node(key, value)
            self.storage[key] = new_node
            self.insert(new_node)