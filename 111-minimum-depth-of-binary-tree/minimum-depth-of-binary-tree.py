# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        
        # empty tree
        if not root:
            return 0
        # tree has 1 node
        elif (not root.left) and (not root.right):
            return 1

        # return value carries depth
        def dfs(node: TreeNode) -> int:
            # base case:
            # 1: left is none and right is none, check min and update
            if (not node.left) and (not node.right):
                return 1

            # 2: only left child
            if (node.left) and (not node.right):
                return 1 + dfs(node.left)
            # 3: only right child
            if (not node.left) and (node.right):
                return 1 + dfs(node.right)

            # 4: if there are both children
            # the shortest path could go to either side,
            # so choose the smaller one
            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)