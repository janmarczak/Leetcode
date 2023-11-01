class Solution:
    def longestPalindrome(self, s: str) -> str:


        # babcba
        # answer: abcba
        # other palindomre: bab

        # 1. Expand Around Center
        # - palindrome mirrors around its center

        if len(s) <= 1:
            return s

        # left -> left center (same as right for odd palindrome)
        # right -> right center (same as left for odd palindrome)
        # s[left] == s[right] make sure that we have a palindrome
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right] # need to add +1 and not do right+1 to "go back"


        max_str = s[0]
        for i in range(len(s)-1):
            odd_pal = expand_from_center(i, i) # same center
            even_pal = expand_from_center(i, i+1) # different centers

            if len(odd_pal) > len(max_str):
                max_str = odd_pal
            if len(even_pal) > len(max_str):
                max_str = even_pal

        return max_str

            # Even palindrome
            # Odd palindrome


        # 2. Brute Force O(n^3)
        # Pick all possile starting and ending positions for a substring and verify if it is a palindrome
        # max_len = 1
        # max_palindrome = s[0]
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1] and j-i+1 > max_len:
        #             max_palindrome = s[i:j+1]
        #             max_len = j-i+1

        # return max_palindrome