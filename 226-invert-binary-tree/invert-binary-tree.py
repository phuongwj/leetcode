# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        if (not root.left) and (not root.right):
            return root
            
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        

        # for every node, swap them by using temp variables,
        # then pass their children if they exist

        # 1. no root
        # if not root:
        #     return None

        # # 2. no children
        # if (not root.left) and (not root.right):
        #     return root

        # def dfs(root: TreeNode) -> TreeNode:
        #     if root.left and (not root.right):
        #         root.right = root.left
        #         root.left = None
        #         dfs(root.right)
                
        #         return root
        #     elif root.right and (not root.left):
        #         root.left = root.right
        #         root.right = None
        #         dfs(root.left)
                
        #         return root

        #     temp_left = root.left
        #     temp_right = root.right

        #     root.left = temp_right
        #     root.right = temp_left
            
        #     if (root.left and root.right):
        #         dfs(root.left)
        #         dfs(root.right)
            
        #     return root

        # return dfs(root)