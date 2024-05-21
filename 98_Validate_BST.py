# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min, max):
            if not node:
                return True
            if min and node.val <= min.val:
                return False
            if max and node.val >= max.val:
                return False
            return dfs(node.left, min, node) and dfs(node.right, node, max)
        return dfs(root, None, None)
