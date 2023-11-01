class Solution:
    def reverse(self, x: int) -> int:

        max_int = pow(2, 31)-1

        reversed_x = 0
        flag = -1 if x < 0 else 1
        x = abs(x)

        while x>0:
            if reversed_x > max_int / 10:
                return 0
            reversed_x = (reversed_x * 10) + x % 10
            x = x // 10


        return reversed_x * flag


        