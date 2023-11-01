class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Input: nums = [4,1,2,1,2]
        # Output: 4

        freq = {}

        for element in nums:
            if element not in freq:
                freq[element] = 1
            else:
                freq[element] += 1
        
        print(freq)

        for key, value in freq.items():
            if value == 1:
                return key

