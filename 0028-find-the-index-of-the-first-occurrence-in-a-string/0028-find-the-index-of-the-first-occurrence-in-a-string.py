class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        ### 1. Naive Approach (O(nm))
        # possible positions (indices) where needle can be in the haystack
        possible_indices = len(haystack) - len(needle) + 1

        for i in range(possible_indices):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                
                if j == len(needle) - 1:
                    return i

        return -1

        ### 2. KMP Algorithm O(m+n)

        ## Create a prefix table 
        # we find the length of the longest proper prefix that is also a suffix 
        # for every prefix in needgle

        # lps = [0] * len(needle)

        # pre = 0
        # for i in range(1, len(needle)):
        #     while (pre > 0 and needle[i] != needle[pre]):
        #         pre = lps[pre-1]
        #     if needle[pre] == needle[i]:
        #         pre += 1
        #         lps[i] = pre


        # # Conduct search


            

        
        