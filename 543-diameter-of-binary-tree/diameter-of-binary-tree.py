# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if (not root.left) and (not root.right):
            return 0

        best = 0
        def dfs(node: TreeNode) -> int:
            nonlocal best

            # if has no children
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            best = max(best, left + right)
            return 1 + max(left, right)

        dfs(root)
        return best