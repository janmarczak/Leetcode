# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)


    def helper(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return True
        if not leftNode or not rightNode:
            return False
        return (
            (leftNode.val == rightNode.val) and 
            (self.helper(leftNode.left, rightNode.right)) and
            (self.helper(leftNode.right, rightNode.left))
        )