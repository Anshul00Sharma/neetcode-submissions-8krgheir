# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        ans = []

        if root:
            que.append(root)
        else:
            return ans
        while len(que) > 0:
            subarr = []
            for _ in range(len(que)):
                val = que.popleft()
                subarr.append(val.val)

                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)
                
            ans.append(subarr)
        return ans

        