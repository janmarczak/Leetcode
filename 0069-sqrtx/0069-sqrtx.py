class Solution:
    def mySqrt(self, x: int) -> int:

        # 0: 0
        # 1 - 3: 1
        # 4 - 8: 2
        # 9 - 15: 3
        # 16 - 24: 4
        # ...
        # X: 17 -> return 4
        # 2 * 2 = 4
        # 3 * 3
        # 4 * 4

        if x == 0:
            return 0

        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2 # 3
            if mid * mid == x: 
                return mid
            elif mid * mid > x:
                last = mid - 1 # 7
            elif mid * mid < x:
                first = mid + 1 # 4
        return last
        
