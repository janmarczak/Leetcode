# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        r1 = self.inorderTraversal(root.left)
        r1.append(root.val)
        r1 += self.inorderTraversal(root.right)
        return r1



#               1
#       2               3
#           4        5      6

# 2 - 4 - 1 - 5 - 3 - 6

        
        