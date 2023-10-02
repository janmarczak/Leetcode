# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        self.preorder(root, pre)
        return pre

    def preorder(self, node, pre):
        if node is None:
            return
        pre.append(node.val)
        self.preorder(node.left, pre)
        self.preorder(node.right, pre)
        