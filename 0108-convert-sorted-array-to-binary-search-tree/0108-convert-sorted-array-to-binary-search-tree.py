# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums))

    # FIRST OPTION (but slicing Operation is O(n))
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]),
            self.sortedArrayToBST(nums[mid_node + 1:])
        )

    # 2ND SOLUTION: Pointers
    # def makeBST(self, nums, start, end):
    #     if start >= end:
    #         return None
    #     mid_node = (start+end) // 2
    #     return TreeNode(
    #         nums[mid_node],
    #         self.makeBST(nums, start, mid_node),
    #         self.makeBST(nums, mid_node + 1, end)
    #     )


# TIME COMPLEXITY: O(N LOG N)
#   The first call processes n elements
#   The next two calls process n/2 elements each
#   The next four calls process n/4 elements each
#   ... and so on
# SPACE COMPLEXITY: O(N)
       






        