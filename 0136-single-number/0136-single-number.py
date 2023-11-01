class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        # Input: nums = [4,1,2,1,2]
        # Output: 4
        elements = set()
        another_elements = set()

        for element in nums:
            if element not in elements:
                elements.add(element)
            else:
                another_elements.add(element)
        # print(another_elements)
        # print((elements - another_elements))

        for element in (elements - another_elements):
            return element
        # return another_elements - elements

        