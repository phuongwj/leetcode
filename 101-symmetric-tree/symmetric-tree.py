# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        # len(input) == 1
        if (root.left is None) and (root.right is None):
            return True

        # len(input) == 2
        if (root.left is None) or (root.right is None):
            return False
        
        def isSymmetric(left: TreeNode, right: TreeNode) -> bool:
            # 1. write the base cases
            # - both nodes are None: return True
            # - 1 node is None: return False
            if (left is None) and (right is None):
                return True
            elif (left is None) or (right is None):
                return False

            # 2. check if not equal
            if left.val != right.val:
                return False

            # 3. outer
            outer = isSymmetric(left.left, right.right)

            # 4. inner
            inner = isSymmetric(left.right, right.left)

            return outer and inner

        return isSymmetric(root.left, root.right)