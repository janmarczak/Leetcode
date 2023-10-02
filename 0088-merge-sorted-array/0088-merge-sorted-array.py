class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        # Output: [1,2,2,3,5,6]

        # 1 - [1,2,3,0,0,6]
        # 2 - [1,2,3,0,5,6]
        # 3 - [1,2,3,3,5,6]

        # 1st: Append and sort:
        # nums1[m:len(nums1)] = nums2 #O(n) n-> length of nums2
        # nums1.sort() # O(m+n log(m+n)) -> same as NlogN but n is the length of merged array

        # 2nd: Using pointers:
        # Pointers of last elements in our arrays
        i, j, k = m-1, n-1, m+n-1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


