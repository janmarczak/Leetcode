# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        post = []
        self.postorder(root, post)
        return post

    def postorder(self, node, post):
        if not node:
            return

        self.postorder(node.left, post)
        self.postorder(node.right, post)
        post.append(node.val)

        