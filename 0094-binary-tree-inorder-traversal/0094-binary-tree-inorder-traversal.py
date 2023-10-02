# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root == None:
        #     return []

        # r1 = self.inorderTraversal(root.left)
        # r1.append(root.val)
        # r1 += self.inorderTraversal(root.right)
        # return r1

        inorder = []
        self.inorder(root, inorder)
        return inorder

    def inorder(self, node, inorder):
        if not node:
            return
        
        self.inorder(node.left, inorder)
        inorder.append(node.val)
        self.inorder(node.right, inorder)

    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []

    #     r1 = [root.val]
    #     r1 += self.preorderTraversal(root.left)
    #     r1 += self.preorderTraversal(root.right)
    #     return r1



#               1
#       2               3
#           4        5      6

# 2 - 4 - 1 - 5 - 3 - 6

        
        