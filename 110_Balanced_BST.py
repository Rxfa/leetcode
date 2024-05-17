# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0
            
            left_node = dfs(node.left)
            right_node = dfs(node.right)
            if abs(left_node-right_node) > 1:
                return -1
            if min(left_node, right_node) == -1:
                return -1
            max_height = max(left_node, right_node)
            return 1 + max_height
            
        return dfs(root) != -1
