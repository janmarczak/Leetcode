class Solution:
    def fib(self, n: int) -> int:

        # 1st solution recursive:
        if n <=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        