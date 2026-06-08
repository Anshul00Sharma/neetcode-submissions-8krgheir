# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p,q)

    def helper(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        left = self.helper(p.left,q.left)
        right = self.helper(p.right,q.right)

        result = left and right and p.val == q.val
        return result