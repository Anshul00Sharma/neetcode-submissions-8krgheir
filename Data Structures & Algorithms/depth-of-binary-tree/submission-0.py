# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxVal = self.helper(root,0)
        return maxVal

    def helper(self, root, maxValue):
        if not root:
            return maxValue
        
        rightMax = self.helper(root.right,maxValue + 1)
        leftMax = self.helper(root.left,maxValue + 1)
        return max(rightMax,leftMax)
        