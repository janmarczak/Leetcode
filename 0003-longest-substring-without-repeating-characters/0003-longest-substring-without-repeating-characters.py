class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        max_length = 0
        left = 0
        indices = {}

        for right in range(n):

            # if the current char is not in the map or its index is less than left, it is a new char
            if s[right] not in indices or indices[s[right]] < left:
                # the indices[s[right]] < left check is there to account for 
                # repeating chars that were before the initial repeating char
                # ex: tmmzuxt (first t when checking the last t)
                indices[s[right]] = right
                max_length = max(max_length, right - left + 1)
            else:
                # char is repeating so left is the position after the last occurance of the char
                left = indices[s[right]] + 1
                indices[s[right]] = right
            
        return max_length

