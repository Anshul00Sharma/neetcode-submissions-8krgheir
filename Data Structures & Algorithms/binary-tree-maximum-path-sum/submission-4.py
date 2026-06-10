class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        def helper(root) -> int:
            nonlocal maxPath
            if not root:
                return 0
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            possibleMax = left + right + root.val
            maxPath = max(maxPath,possibleMax)
            return max(left + root.val,right + root.val)
        helper(root)
        return maxPath