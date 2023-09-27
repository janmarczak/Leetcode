class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1 # index where a unique element should be placed
        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]: # elements are unique
            # placing it in j (we don't care what happens to number at j because it's a duplicate)
                nums[j] = nums[i] 
                j += 1
        return j




        
        