class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 1. HashMap
        # Time: O(n)
        # Space: O(n)

        # freq = {}
        # for n in nums:
        #     if n not in freq:
        #         freq[n] = 1
        #     else:
        #         freq[n] += 1

        #     if freq[n] > (len(nums) / 2):
        #         return n

        # 2. Sort the array
        # Time: O(N Log N)
        # Space: O(1)
        nums = sorted(nums)
        return nums[int((len(nums)/2))]
        # max_count = 1
        # majority_element = nums[0]
        # count = 1
        # element = nums[0]
        # for i in range(1, len(nums)):
        #     print(nums[i])
        #     if nums[i] == element:
        #         count += 1
        #     else:
        #         element = nums[i]
        #         count = 1

        #     if count > max_count:
        #             max_count = count
        #             majority_element = element
        # return majority_element


        

        