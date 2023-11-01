class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        ###### 1. Frequency Map
        # Time: O(n)
        # Space: O(n)

        # freq = {}

        # for element in nums:
        #     if element not in freq:
        #         freq[element] = 1
        #     else:
        #         freq[element] += 1

        # for key, value in freq.items():
        #     if value == 1:
        #         return key

        ###### 2. XOR
        # Time: O(N)
        # Space: O(1)
        # Elements with frequency 2 will result in 0. 
        # And the only element with frequency 1 will generate the answer (itself)

        # A	B	A⊕B
        # 1	1	0
        # 0	1	1
        # 1	0	1
        # 0	0	0

        answer = 0
        for element in nums:
            answer = answer ^ element
        return answer




