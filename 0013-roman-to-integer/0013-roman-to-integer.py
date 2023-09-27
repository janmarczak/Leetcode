class Solution:
    def romanToInt(self, s: str) -> int:

        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0
        for i, char in enumerate(s):
            if i < len(s) - 1 and romans[char] < romans[s[i+1]]:
                sum -= romans[char]
            else:
                sum += romans[char]

        return sum
