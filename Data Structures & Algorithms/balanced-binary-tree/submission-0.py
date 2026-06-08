class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.helper(root)
        return ans[0]
    
    def helper(self, root) -> list:
        if not root:
            return [True,0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        finalHeight = 1 + max(left[1],right[1])
        balanced = (abs(left[1] - right[1]) <= 1) and left[0] and right[0]

        return [balanced,finalHeight]