# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lt = []
        def help(root):
            nonlocal lt
            if not root:
                return
            help(root.left)
            lt.append(root.val)
            help(root.right)
        help(root)
        for i in range(len(lt)-1):
            if lt[i]>=lt[i+1]:
                return False
        return True