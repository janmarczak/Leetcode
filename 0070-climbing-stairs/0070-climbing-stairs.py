class Solution:
    def climbStairs(self, n: int, cache=None) -> int:

        # First solution: Too long
        # if n <= 0:
        #     return 0
        # elif n == 1 or n == 2:  
        #     return n
        # else: 
        #     results1 = self.climbStairs(n - 1) 
        #     results2 = self.climbStairs(n - 2) 
        # return results1 + results2

        # Second Solution: Memoisation
        if cache is None:
            cache = {
                0: 0,
                1: 1,
                2: 2,
            }

        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)
        return cache[n]


        ##### 5
        # 1. r1 = climbStairs(4)
        #   1.1 r1 = climbStairs(3)
        #       1.1.1 r1 = climbStairs(2)
        #           return 2
        #       1.1.2 r2 = climbStairs(1)
        #            return 1
        #   1.2 r2 = climbStairs(2)
        #       return 2
        # 2. r2 = climbStairs(3)
        #   2.1. = climbStairs(2)
        #       return 2
        #   2.2. = climbStairs(1)
        #       return 1
    