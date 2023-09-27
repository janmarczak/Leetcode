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
        last_char = ''
        for char in s:
            if (char == 'V' or char == 'X') and last_char == 'I':
                sum -= 2 * romans[last_char]
            elif (char == 'L' or char == 'C') and last_char == 'X':
                sum -= 2 * romans[last_char]
            elif (char == 'D' or char == 'M') and last_char == 'C':
                sum -= 2 * romans[last_char]

            sum += romans[char]
            last_char = char


        return sum
