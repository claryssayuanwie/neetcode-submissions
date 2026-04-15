# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left # move 
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res[k-1]

