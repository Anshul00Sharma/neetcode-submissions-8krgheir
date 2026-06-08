class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root,subRoot)
    
    def helper(self,root , subRoot):
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        left = self.helper(root.left,subRoot)
        right = self.helper(root.right,subRoot)
        return left or right

    def sameTree(self, t1,t2):
        if not t2 and not t1:
            return True
        if not t2 or not t1:
            return False
        left = self.sameTree(t1.left,t2.left)
        right = self.sameTree(t1.right,t2.right)
        result = left and right and t1.val == t2.val
        
        return result