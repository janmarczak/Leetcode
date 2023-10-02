class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        # 0: 0
        # 1 - 3: 1
        # 4 - 8: 2
        # 9 - 15: 3
        # 16 - 24: 4
        # ...

        for n in range(1, x+1):
            if n * n == x:
                return n
            elif n * n > x:
                return n-1
        