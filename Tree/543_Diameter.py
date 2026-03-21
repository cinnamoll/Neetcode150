# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def treeLen(curr) -> int:
            if curr is None:
                return 0

            left = treeLen(curr.left)
            right = treeLen(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        treeLen(root)
        return self.res