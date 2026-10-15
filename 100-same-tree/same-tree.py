# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # pop one node from each queue per step and compare them

        queueP = []
        queueQ = []

        queueP.append(p)
        queueQ.append(q)

        while queueP and queueQ:
            topP = queueP.pop(0)
            topQ = queueQ.pop(0)

            # They match, and there could still be other nodes in the queues
            # you haven't compared yet. 
            if (not topP) and (not topQ):
                continue

            if (not topP) or (not topQ) or topP.val != topQ.val:
                return False

            if topP.left:
                queueP.append(topP.left)
            else:
                queueP.append(None)

            if topP.right:
                queueP.append(topP.right)
            else:
                queueP.append(None)

            if topQ.left:
                queueQ.append(topQ.left)
            else:
                queueQ.append(None)

            if topQ.right:
                queueQ.append(topQ.right)
            else:
                queueQ.append(None)

            print("Queue P is: ", queueP)
            print("Queue Q is: ", queueQ)

        return True