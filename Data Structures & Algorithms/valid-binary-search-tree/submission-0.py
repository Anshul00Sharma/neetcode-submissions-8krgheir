class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, minl, maxl):
        if not root:
            return True
        if root.val >= maxl or root.val <= minl:
            return False
        left = self.helper(root.left, minl, root.val)
        right = self.helper(root.right, root.val, maxl)

        return left and right
