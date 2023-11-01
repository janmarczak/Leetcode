class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ### 1. Moore Voting Algorithm
        # - majority element will always be in the lead even after
        # encountering other elements
        # Time: O(n)
        # Space: O(1)

        count = 0
        candidate = 0

        for n in nums:
            if count == 0:
                candidate = n

            if n == candidate:
                count += 1
            else:
                count -=1

        return candidate


        ### 2. HashMap
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

        ### 3. Sort the array and take the middle element
        # Time: O(N Log N)
        # Space: O(1)
        # nnums.sort()
        # n = len(nums)
        # return nums[n//2]

        