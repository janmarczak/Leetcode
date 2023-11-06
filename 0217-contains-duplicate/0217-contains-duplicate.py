class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Time: O(N), Space: O(1)
        # 
        nums = sorted(nums)

        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]

        return False
        