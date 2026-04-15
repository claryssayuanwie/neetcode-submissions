# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if node.right == null or node.left == null, return none
        # preorder - root > layer 1 > layer 2
        # inorder - left > right
        if not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid + 1:])

        return root