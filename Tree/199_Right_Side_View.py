# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = []
        res = []

        q.append(root)
        while q:
            len_q = len(q)
            lvl_order = []
            for _ in range(len_q):
                node = q.pop(0)
                lvl_order.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(lvl_order[-1])
        return res