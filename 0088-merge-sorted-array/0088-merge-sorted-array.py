class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Input: nums1 = [2,5,6,0,0,0], m = 3, nums2 = [1,2,7], n = 3
        # Output: [1,2,2,5,6,7]

        # 1st: Append and sort:
        nums1[m:len(nums1)] = nums2
        nums1.sort()

        # j = 0
        # for i in range(len(nums1)):
        #     print(nums1, nums2)
        #     print(i, j)
        #     if nums2[j] <= nums1[i]:
        #         nums1[i+1:m+1] = nums1[i:m]
        #         nums1[i] = nums2[j]
        #         j += 1
        #         print(nums1)
        #     elif i > m:
        #         nums1[i:] = nums2[j:]
        #         print(nums1, nums2)
        #         return
