class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.helper(root,p,q)

    def helper(self,root,p,q):
        if not root:
            return root
        if root.val > p.val and root.val > q.val:
            return self.helper(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            return self.helper(root.right,p,q)
        else:
            return root