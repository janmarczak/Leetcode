class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        max_length = 0
        left = 0
        indices = {}

        for right in range(n):

            # if the current char is not in the map or its index is less than left, it is a new char
            if s[right] not in indices or indices[s[right]] < left:
                indices[s[right]] = right
                max_length = max(max_length, right - left + 1)
            else:
                # char is repeating so we move the left to the next position after the last occurance of the char
                left = indices[s[right]] + 1
                indices[s[right]] = right # update the index

            # if s[i] not in indices:
            #     indices[s[i]] = i
            #     length += 1
            # else:
            #     max_length = max(length, max_length)
            #     length -= (indices[s[i]])
            #     indices = {}
            #     indices[s[i]] = i

        # abcabcbb
        # l=1, ml=0, {a: 0}
        # l=2, ml=0, {a: 0, b: 1}
        # l=3, ml=0, {a: 0, b: 1, c:2}
        # l=3, ml=3, {a: 0, b: 1, c:2}
                

        # tmmzuxt
        # l=1 , ml=, {t: 0}
        # l=2 , ml=, {t: 0, m: 1}
        # l=1 , ml=2, {t: 0, m: 2}
        # l=2 , ml=2, {t: 0, m: 2, z: 3}
        # l=3 , ml=2, {t: 0, m: 2, z: 3, u: 4}
        # l=4 , ml=2, {t: 0, m: 2, z: 3, u: 4, x: 5}
        # l=4 , ml=2, {t: 0, m: 2, z: 3, u: 4, x: 5}

        # pwwkew
        # {p: 0}, l=1, ml=0
        # {p: 0, w: 1}, l=2, ml=0
        # {p: 0, w: 2}, l=1, ml=2
        # {p: 0, w: 2, k: 3}, l=2, ml=2
        # {p: 0, w: 2, k: 3, e: 4}, l=3, ml=2
        # {p: 0, w: 2, k: 3, e: 4}, l=3, ml=3
            

        return max_length
                # a: 0
                # b: 1
                # c: 2
                # length = 3

        


        # abcadb

        # bcad -> 4

        # abcbda

        # a: 0
        # b: 1
        # c: 2

        # abcbad

        # a: 0
        # b: 1
        # c: 2
        # 

        # HashMap of character to indices