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
        result = []
        queue = deque([root])
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft() # remove from queue then append to levek answer
                level.append(node.val)
                if node.left: # add left child to queue to build next layer
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
