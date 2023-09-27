class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # possible positions (indices) where needle can be in the haystack
        possible_positions = len(haystack) - len(needle) + 1

        for i in range(possible_positions):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                
                if j == len(needle) - 1:
                    return i

        return -1


            

        
        