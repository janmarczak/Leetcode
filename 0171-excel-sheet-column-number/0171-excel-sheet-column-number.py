class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # translating. base 26 to decimal number
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64 # get the digit (ex: Z=26)
            ans += digit * 26**pos
            pos += 1
        return ans

        # We do the same but for Base 26
        # number = '2539'
        # ans = 0                   0
        # ans = ans + 9 * 10**0     9
        # ans = ans + 3 * 10**1     39
        # ans = ans + 5 * 10**2     539
        # ans = ans + 2 * 10**3     2539
 