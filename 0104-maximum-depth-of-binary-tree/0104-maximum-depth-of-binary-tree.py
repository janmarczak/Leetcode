# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # RECURSIVELY:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:        
    #     if not root:
    #         return 0

    #     depth = 0

    #     return max(depth + 1 + self.maxDepth(root.left), depth + 1 + self.maxDepth(root.right))
        
    # ITERATIVELY
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return max_depth




