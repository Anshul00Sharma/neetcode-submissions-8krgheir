# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def helper(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            right = helper(root.right)
            left = helper(root.left)
            maxDiameter = max(maxDiameter,right+left) 
            return 1+ max(right,left)
        helper(root)
        return maxDiameter


    