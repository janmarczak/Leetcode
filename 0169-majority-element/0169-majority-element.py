class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 1. HashMap

        # freq = {}
        # for n in nums:
        #     if n not in nums:
        #         freq[n] = 1
        #     else:
        #         freq[n] += 1

        # [2,2,1,1,1,2,2]

        # 1. Sort the array
        nums = sorted(nums)
        max_count = 1
        majority_element = nums[0]
        count = 1
        element = nums[0]
        for i in range(1, len(nums)):
            print(nums[i])
            if nums[i] == element:
                count += 1
            else:
                element = nums[i]
                count = 1

            if count > max_count:
                    max_count = count
                    majority_element = element
        return majority_element


        

        