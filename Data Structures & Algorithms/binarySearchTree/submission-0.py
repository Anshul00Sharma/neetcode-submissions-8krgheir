class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None
        
    def insert(self, key: int, val: int) -> None:        
        if not self.root:
            self.root = TreeNode(key,val)
            return
        cur = self.root
        while True:
            if key > cur.key:
                if not cur.right:
                    cur.right = TreeNode(key,val)
                    return
                cur = cur.right
            elif key < cur.key:
                if not cur.left:
                    cur.left = TreeNode(key,val)
                    return
                cur = cur.left
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        if not cur:
            return -1
        while cur:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.val
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        return self.getMinHelper(self.root).val
    
    def getMinHelper(self, node) -> TreeNode:
        if not node.left:
            return node
        
        return self.getMinHelper(node.left)



    def getMax(self) -> int:
        if not self.root:
            return -1
        return self.getMaxHelper(self.root)
    
    def getMaxHelper(self, node) -> int:
        if not node.right:
            return node.val
        
        return self.getMaxHelper(node.right)


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self,node,key):
        if not node:
            return None
        if key > node.key:
            node.right = self.removeHelper(node.right, key)
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                minN = self.getMinHelper(node.right)
                node.key = minN.key
                node.val = minN.val
                node.right = self.removeHelper(node.right,minN.key)
        
        return node


    def getInorderKeys(self) -> List[int]:
        self.arr = []
        self.getInorderHelper(self.root)
        return self.arr

    def getInorderHelper(self,node):
        if not node:
            return
        self.getInorderHelper(node.left)
        self.arr.append(node.key)
        self.getInorderHelper(node.right)