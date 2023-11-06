class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums = sorted(nums)

        # [1,2,3,1] -> 1 1 2 3 

        for i in range(len(nums)):
            if i != len(nums) - 1 and nums[i] == nums[i+1]:
                return True
        
        return False
        