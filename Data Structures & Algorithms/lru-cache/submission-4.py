class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.storage = {}

    def get(self, key: int) -> int:
        if key in self.storage:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.storage[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage[key] = value
            self.queue.remove(key)
            self.queue.appendleft(key)
        else:
            if len(self.queue) < self.capacity:
                self.storage[key] = value
                self.queue.appendleft(key)
            else:
                lastKey = self.queue.pop()
                del self.storage[lastKey]
                self.storage[key] = value
                self.queue.appendleft(key)