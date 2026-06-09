class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            stack = []
            count = 0
            while root or stack:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    cur = stack.pop()
                    count += 1
                    if count == k:
                        return cur.val
                    root = cur.right
            return 0
        return inorder(root)