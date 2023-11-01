class Solution:
    def longestPalindrome(self, s: str) -> str:


        # babcba
        # answer: abcba
        # other palindomre: bab

        # 1. Brute Force O(n^3)
        # Pick all possile starting and ending positions for a substring and verify if it is a palindrome
        # max_len = 1
        # max_palindrome = s[0]
        # for i in range(len(s)-1):
        #     for j in range(i+1, len(s)):
        #         print(s[i:j+1], s[i:j+1][::-1])
        #         if s[i:j+1] == s[i:j+1][::-1] and j-i+1 > max_len:
        #             max_palindrome = s[i:j+1]
        #             max_len = j-i+1

        # return max_palindrome

        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str