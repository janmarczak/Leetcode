class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1. Brute Force Approach
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 2. HashMap
        numMap = {}
        n = len(nums)

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []




        