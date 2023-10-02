class Solution:
    def fib(self, n: int) -> int:

        # 1st solution recursive:
        # if n <=1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
    
        cache = {
                0: 0,
                1: 1,
            }
        return self.recursive_helper(n, cache)
        
    # 2nd Memoization:
    def recursive_helper(self, n: int, cache) -> int:
        if n in cache:
            return cache[n]
        return self.recursive_helper(n-1, cache) + self.recursive_helper(n-2, cache)

