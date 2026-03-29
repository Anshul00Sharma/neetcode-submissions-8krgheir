class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashT = {}

        def dfs(node):
            if node in hashT:
                return hashT[node]
            
            copy = Node(node.val)
            hashT[node] = copy
            for nd in node.neighbors:
                copy.neighbors.append(dfs(nd))
            return copy
        
        return dfs(node)