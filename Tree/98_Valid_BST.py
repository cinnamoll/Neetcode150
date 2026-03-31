# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, prev):
        if root is None:
            return True
        if not self.inorder(root.left, prev):
            return False
        if prev[0] >= root.val:
            return False
        prev[0] = root.val
        return self.inorder(root.right, prev)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [float('-inf')]
        return self.inorder(root, prev)