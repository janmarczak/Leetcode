class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Time: O(N), Space: O(1)
        # nums = sorted(nums)

        # prev = None
        # for i in range(len(nums)):
        #     if nums[i] == prev:
        #         return True
        #     prev = nums[i]

        # return False

        # Time: 
        # Space: 

        unique_values = set()

        for num in nums:
            if num in unique_values:
                return True
            
            unique_values.add(num)

        return False

        