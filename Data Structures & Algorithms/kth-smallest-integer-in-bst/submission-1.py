class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = 0
        count = 0

        def inorderT(root):
            nonlocal ans, count
            if not root or ans != 0:
                return
            inorderT(root.left)
            count += 1
            if count == k:
                ans = root.val
                return
            inorderT(root.right)

        inorderT(root)
        return ans