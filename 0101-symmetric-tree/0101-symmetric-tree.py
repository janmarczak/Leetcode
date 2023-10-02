from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # # RECURSIVE SOUTION:
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     return self.isSame(root.left, root.right)

    # def isSame(self, leftNode, rightNode):
    #     if not leftNode and not rightNode:
    #         return True
    #     if not leftNode or not rightNode:
    #         return False
    #     return (
    #         (leftNode.val == rightNode.val) and 
    #         (self.isSame(leftNode.left, rightNode.right)) and
    #         (self.isSame(leftNode.right, rightNode.left))
    #     )

    # ITERATIVE SOLUTION:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Use two queues to traverse the left and right subtrees.
        left_queue = deque([root.left])
        right_queue = deque([root.right])
        
        while left_queue and right_queue:
            left_node = left_queue.popleft()
            right_node = right_queue.popleft()
            
            # If both nodes are None, continue the loop.
            if not left_node and not right_node:
                continue
            
            # If one of them is None (but not both), return False.
            if not left_node or not right_node:
                return False
            
            # Check if values are different.
            if left_node.val != right_node.val:
                return False
            
            # Enqueue children in appropriate order for checking symmetry.
            left_queue.append(left_node.left)
            left_queue.append(left_node.right)
            right_queue.append(right_node.right)
            right_queue.append(right_node.left)
            
        return True



    # TIME: O(N) where N is the number of nodes. We need to visit each node once if it's symmetric
    # SPACE: O(h), where h is the height of the tree. In the worst case, the tree can be completely    unbalanced, and the recursion stack can go as deep as the height of the tree.