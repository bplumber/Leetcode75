# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append([root])
        main = []
        temp = []
        tp = []
        while q:
            node = q.popleft()
            for i in node:
                temp.append(i.val)
                if i.left:
                    tp.append(i.left)     
                if i.right:
                    tp.append(i.right)
            if len(tp)!=0:
                q.append(tp)
                tp = []
            main.append(temp)
            temp = []
        return main