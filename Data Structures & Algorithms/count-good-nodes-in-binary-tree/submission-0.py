# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root,maxVal):
            nonlocal count
            if not root:
                return None
            if root.val >= maxVal:
                count += 1
                maxVal = root.val
            helper(root.left,maxVal)
            helper(root.right,maxVal)
        helper(root,float('-inf'))
        return count 
            

        