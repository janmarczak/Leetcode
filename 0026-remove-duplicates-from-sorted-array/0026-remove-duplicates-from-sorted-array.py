class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        # last_number = None # 0
        # indices = []
        # for i, val in enumerate(nums):
        #     if last_number == val:
        #         indices.append(i)
        #     else:
        #         last_number = nums[i]

        # k = len(nums) - len(indices)
        # for i in reversed(indices):
        #     nums.append(nums.pop(i))

        # return k

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j




        
        