# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return True
        if not leftNode or not rightNode:
            return False
        return (
            (leftNode.val == rightNode.val) and 
            (self.isSame(leftNode.left, rightNode.right)) and
            (self.isSame(leftNode.right, rightNode.left))
        )