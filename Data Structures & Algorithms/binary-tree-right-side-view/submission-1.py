# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightArr = []
        que = deque()

        if root:
            que.append(root)
        else:
            return rightArr
        while len(que) > 0:
            subArr = []
            for _ in range(len(que)):
                node = que.popleft()
                subArr.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            rightArr.append(subArr[-1])
        
        return rightArr
         
            
        