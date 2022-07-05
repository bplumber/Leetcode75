# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rt = None
        def hlp(root):
            nonlocal rt
            if not root:
                return
            print(p.val, root.val, q.val)
            if (root.val >= p.val and root.val <=q.val) or (root.val <= p.val and root.val >=q.val):
                rt = root
            elif root.val >= p.val and root.val>=q.val:
                hlp(root.left)
            elif root.val <=p.val and root.val <= q.val:
                hlp(root.right)
        hlp(root)
        return rt
                
                