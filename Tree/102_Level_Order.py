# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = []
        res = []
        q.append(root)
        curr_lvl = 0

        while q:
            q_len = len(q)
            res.append([])
            for _ in range (q_len):
                node = q.pop(0)
                res[curr_lvl].append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            curr_lvl += 1
        return res